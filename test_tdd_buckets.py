import unittest
import tdd_buckets

class chargeRangeReadingsTest(unittest.TestCase):
  
  def test(self):
    self.assertTrue(tdd_buckets.getFreqOfChargeRanges([], tdd_buckets.ADC_12Bit) == "")
    self.assertTrue(tdd_buckets.getFreqOfChargeRanges([0], tdd_buckets.ADC_12Bit) == "0-0, 1\n")
    self.assertTrue(tdd_buckets.getFreqOfChargeRanges([4094], tdd_buckets.ADC_12Bit) == "10-10, 1\n")
    self.assertTrue(tdd_buckets.getFreqOfChargeRanges([4094,4095], tdd_buckets.ADC_12Bit) == "10-10, 1\n")#ignore error readings
    self.assertTrue(tdd_buckets.getFreqOfChargeRanges([0,4000], tdd_buckets.ADC_12Bit) == "0-0, 1\n10-10, 1\n")
    
    
    
    self.assertTrue(tdd_buckets.getFreqOfChargeRanges([],tdd_buckets.ADC_10Bit) == "")
    self.assertTrue(tdd_buckets.getFreqOfChargeRanges([0], tdd_buckets.ADC_10Bit) == "15-15, 1\n")
    self.assertTrue(tdd_buckets.getFreqOfChargeRanges([511], tdd_buckets.ADC_10Bit) == "0-0, 1\n")
    self.assertTrue(tdd_buckets.getFreqOfChargeRanges([1022], tdd_buckets.ADC_10Bit) == "15-15, 1\n")
    self.assertTrue(tdd_buckets.getFreqOfChargeRanges([1022,1023], tdd_buckets.ADC_10Bit) == "15-15, 1\n")#ignore error readings
    self.assertTrue(tdd_buckets.getFreqOfChargeRanges([0,100,150,300,500,70,1500,700,600,2000,1022], tdd_buckets.ADC_10Bit) == "0-0, 1\n3-3, 1\n6-6, 2\n11-13, 3\n15-15, 2\n")

    
unittest.main()
