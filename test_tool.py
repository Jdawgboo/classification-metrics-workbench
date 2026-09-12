import unittest
from tool import report
class MetricsTests(unittest.TestCase):
 def test_metrics(self):
  result=report(['a','a','b'],['a','b','b']); self.assertAlmostEqual(result['accuracy'],2/3); self.assertEqual(result['per_class']['a']['precision'],1.0); self.assertEqual(result['per_class']['a']['recall'],0.5)
if __name__=='__main__': unittest.main()
