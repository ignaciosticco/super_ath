/* ----------------------------------------------------------------------
   LAMMPS - Large-scale Atomic/Molecular Massively Parallel Simulator
   http://lammps.sandia.gov, Sandia National Laboratories
   Steve Plimpton, sjplimp@sandia.gov

   Copyright (2003) Sandia Corporation.  Under the terms of Contract
   DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains
   certain rights in this software.  This software is distributed under
   the GNU General Public License.

   See the README file in the top-level LAMMPS directory.
------------------------------------------------------------------------- */

#include "math.h"
#include "string.h"
#include "stdlib.h"
#include "compute_granular_helbing_atom.h"
#include "atom.h"
#include "update.h"
#include "modify.h"
#include "neighbor.h"
#include "neigh_list.h"
#include "neigh_request.h"
#include "force.h"
#include "pair.h"
#include "comm.h"
#include "memory.h"
#include "error.h"

#include "group.h"

#define DIAM 0.6


using namespace LAMMPS_NS;

/* ---------------------------------------------------------------------- */

ComputeGranularHelbingAtom::ComputeGranularHelbingAtom(LAMMPS *lmp, int narg, char **arg) :
  Compute(lmp, narg, arg)
{
  if (narg != 3) error->all(FLERR,"Illegal compute granular_helbing/atom command");

  peratom_flag = 1;
  size_peratom_cols = 0;
  comm_forward = 1;

  nmax = 0;
  clusterID = NULL;
}

/* ---------------------------------------------------------------------- */

ComputeGranularHelbingAtom::~ComputeGranularHelbingAtom()
{
  memory->destroy(clusterID);
}

/* ---------------------------------------------------------------------- */

void ComputeGranularHelbingAtom::init()
{
  if (atom->tag_enable == 0)
    error->all(FLERR,"Cannot use compute granular_helbing/atom unless atoms have IDs");
  if (force->pair == NULL)
    error->all(FLERR,"Compute granular_helbing/atom requires a pair style be defined");

  // need an occasional full neighbor list
  // full required so that pair of atoms on 2 procs both set their clusterID

  int irequest = neighbor->request(this,instance_me);
  neighbor->requests[irequest]->pair = 0;
  neighbor->requests[irequest]->compute = 1;
  neighbor->requests[irequest]->half = 0;
  neighbor->requests[irequest]->full = 1;
  neighbor->requests[irequest]->occasional = 1;

  int count = 0;
  for (int i = 0; i < modify->ncompute; i++)
    if (strcmp(modify->compute[i]->style,"granular_helbing/atom") == 0) count++;
  if (count > 1 && comm->me == 0)
    error->warning(FLERR,"More than one compute granular_helbing/atom");
}

/* ---------------------------------------------------------------------- */

void ComputeGranularHelbingAtom::init_list(int id, NeighList *ptr)
{
  list = ptr;
}

/* ---------------------------------------------------------------------- */

void ComputeGranularHelbingAtom::compute_peratom()
{
  int i,j,ii,jj,inum,jnum;
  double xtmp,ytmp,ztmp,delx,dely,delz,r;
  int *ilist,*jlist,*numneigh,**firstneigh;

  invoked_peratom = update->ntimestep;

  // grow clusterID array if necessary

  if (atom->nlocal+atom->nghost > nmax) {
    memory->destroy(clusterID);
    nmax = atom->nmax;
    memory->create(clusterID,nmax,"granular_helbing/atom:clusterID");
    vector_atom = clusterID;
  }

  // invoke full neighbor list (will copy or build if necessary)

  neighbor->build_one(list);

  inum = list->inum;
  ilist = list->ilist;
  numneigh = list->numneigh;
  firstneigh = list->firstneigh;

  // if group is dynamic, insure ghost atom masks are current

  if (group->dynamic[igroup]) {
    commflag = 0;
    comm->forward_comm_compute(this);
  }

  // every atom starts in its own cluster, with clusterID = atomID

  int *mask = atom->mask;

  for (ii = 0; ii < inum; ii++) {
    i = ilist[ii];
    if (mask[i] & groupbit) clusterID[i] = 0.0;
    else clusterID[i] = 0.0;
  }

  // loop until no more changes on any proc:
  // acquire clusterIDs of ghost atoms
  // loop over my atoms, checking distance to neighbors
  // if both atoms are in cluster, assign lowest clusterID to both
  // iterate until no changes in my atoms
  // then check if any proc made changes

  commflag = 1;
  double **x = atom->x;

  int change,done,anychange;

  while (1) {
    comm->forward_comm_compute(this);

    change = 0;
    while (1) {
      done = 1;
      for (ii = 0; ii < inum; ii++) {
        i = ilist[ii];
        if (!(mask[i] & groupbit)) continue;

        xtmp = x[i][0];
        ytmp = x[i][1];
        ztmp = x[i][2];
        jlist = firstneigh[i];
        jnum = numneigh[i];

        for (jj = 0; jj < jnum; jj++) {
          j = jlist[jj];
          j &= NEIGHMASK;
          if (!(mask[j] & groupbit)) continue;
          //if (clusterID[i] == clusterID[j]) continue;

          delx = xtmp - x[j][0];
          dely = ytmp - x[j][1];
          delz = ztmp - x[j][2];
          r = sqrt(delx*delx + dely*dely + delz*delz);

          clusterID[i]+=2000.0*exp((DIAM-r)/0.08)*r;
        }
      }
      if (!done) change = 1;
      if (done) break;
    }

    // stop if all procs are done

    MPI_Allreduce(&change,&anychange,1,MPI_INT,MPI_MAX,world);
    if (!anychange) break;
  }
}

/* ---------------------------------------------------------------------- */

int ComputeGranularHelbingAtom::pack_forward_comm(int n, int *list, double *buf,
                                          int pbc_flag, int *pbc)
{
  int i,j,m;

  m = 0;
  if (commflag) {
    for (i = 0; i < n; i++) {
      j = list[i];
      buf[m++] = clusterID[j];
    }
  } else {
    int *mask = atom->mask;
    for (i = 0; i < n; i++) {
      j = list[i];
      buf[m++] = ubuf(mask[j]).d;
    }
  }

  return m;
}

/* ---------------------------------------------------------------------- */

void ComputeGranularHelbingAtom::unpack_forward_comm(int n, int first, double *buf)
{
  int i,m,last;

  m = 0;
  last = first + n;
  if (commflag)
    for (i = first; i < last; i++) clusterID[i] = buf[m++];
  else {
    int *mask = atom->mask;
    for (i = first; i < last; i++) mask[i] = (int) ubuf(buf[m++]).i;
  }
}

/* ----------------------------------------------------------------------
   memory usage of local atom-based array
------------------------------------------------------------------------- */

double ComputeGranularHelbingAtom::memory_usage()
{
  double bytes = nmax * sizeof(double);
  return bytes;
}
