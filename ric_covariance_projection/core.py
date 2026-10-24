import math,itertools
from .common import number

def vector(v):
 if not isinstance(v,list)or len(v)!=3:raise ValueError('vector3')
 return [number(x,-1e15,1e15)for x in v]
def dot(a,b):return math.fsum(x*y for x,y in zip(a,b))
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def unit(v):
 n=math.sqrt(dot(v,v))
 if n==0:raise ValueError('degenerate_frame')
 return [x/n for x in v]
def det(m):
 if len(m)==1:return m[0][0]
 return sum((-1)**j*m[0][j]*det([r[:j]+r[j+1:]for r in m[1:]])for j in range(len(m)))
def run(data):
 position=vector(data['position']);velocity=vector(data['velocity']);radial=unit(position);normal=unit(cross(radial,unit(velocity)));along=cross(normal,radial);rotation=[radial,along,normal]
 P=[vector(r)for r in data['covariance']]
 if len(P)!=3:raise ValueError('matrix3')
 scale=max(1,max(abs(x)for row in P for x in row));tol=1e-10
 if any(abs(P[i][j]-P[j][i])>tol*scale for i in range(3)for j in range(3)):raise ValueError('symmetry')
 P=[[(P[i][j]+P[j][i])/2 for j in range(3)]for i in range(3)]
 for k in range(1,4):
  for ids in itertools.combinations(range(3),k):
   if det([[P[i][j]for j in ids]for i in ids]) < -tol*scale**k:raise ValueError('not_psd')
 transformed=[[math.fsum(rotation[i][a]*P[a][b]*rotation[j][b]for a in range(3)for b in range(3))for j in range(3)]for i in range(3)]
 return {'rotation_inertial_to_ric':rotation,'position_covariance_ric':transformed,'trace_before':sum(P[i][i]for i in range(3)),'trace_after':sum(transformed[i][i]for i in range(3)),'model':'instantaneous_position_covariance_projection_only','psd_tolerance_relative':tol}
