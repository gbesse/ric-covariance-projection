import unittest,math
from ric_covariance_projection import run
class Tests(unittest.TestCase):
 def test_known_ninety_degree_frame(self):
  r=run({'position':[0,2,0],'velocity':[-1,0,0],'covariance':[[4,1,0],[1,9,0],[0,0,16]]});self.assertEqual(r['position_covariance_ric'],[[9.0,-1.0,0.0],[-1.0,4.0,0.0],[0.0,0.0,16.0]])
 def test_isotropic_covariance_and_orthonormality(self):
  r=run({'position':[1,2,3],'velocity':[4,0,1],'covariance':[[7,0,0],[0,7,0],[0,0,7]]});R=r['rotation_inertial_to_ric']
  for i in range(3):
   for j in range(3):self.assertAlmostEqual(sum(R[i][k]*R[j][k]for k in range(3)),float(i==j));self.assertAlmostEqual(r['position_covariance_ric'][i][j],7*float(i==j))
 def test_quadratic_form_independent_projection(self):
  p=[[2,1,0],[1,3,0],[0,0,4]];r=run({'position':[1,1,0],'velocity':[0,1,1],'covariance':p});u=[2,-1,3];R=r['rotation_inertial_to_ric'];v=[sum(R[i][j]*u[i]for i in range(3))for j in range(3)];self.assertAlmostEqual(sum(u[i]*r['position_covariance_ric'][i][j]*u[j]for i in range(3)for j in range(3)),sum(v[i]*p[i][j]*v[j]for i in range(3)for j in range(3)))
 def test_non_psd_asymmetric_and_degenerate_rejected(self):
  for p in [[[-1,0,0],[0,1,0],[0,0,1]],[[1,2,0],[2,1,0],[0,0,1]],[[1,1,0],[0,1,0],[0,0,1]]]:
   with self.assertRaises(ValueError):run({'position':[1,0,0],'velocity':[0,1,0],'covariance':p})
  with self.assertRaises(ValueError):run({'position':[1,0,0],'velocity':[2,0,0],'covariance':[[1,0,0],[0,1,0],[0,0,1]]})
