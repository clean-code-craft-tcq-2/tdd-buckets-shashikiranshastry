import unittest
import tdd_buckets

class chargeRangeReadingsTest(unittest.TestCase):
  
  def test(self):
    self.assertTrue(tdd_buckets.getFreqOfChargeRanges([], chargeRangeReadings.ADC_12Bit) == "")
    self.assertTrue(tdd_buckets.getFreqOfChargeRanges([0], chargeRangeReadings.ADC_12Bit) == "0-0, 1\n")
    self.assertTrue(tdd_buckets.getFreqOfChargeRanges([4094], chargeRangeReadings.ADC_12Bit) == "10-10, 1\n")
    self.assertTrue(tdd_buckets.getFreqOfChargeRanges([4094,4095], chargeRangeReadings.ADC_12Bit) == "10-10, 1\n")#ignore error readings
    self.assertTrue(tdd_buckets.getFreqOfChargeRanges([0,4000], chargeRangeReadings.ADC_12Bit) == "0-0, 1\n10-10, 1\n")
    
    
    
    self.assertTrue(tdd_buckets.getFreqOfChargeRanges([], chargeRangeReadings.ADC_10Bit) == "")
    self.assertTrue(tdd_buckets.getFreqOfChargeRanges([0], chargeRangeReadings.ADC_10Bit) == "15-15, 1\n")
    self.assertTrue(tdd_buckets.getFreqOfChargeRanges([511], chargeRangeReadings.ADC_10Bit) == "0-0, 1\n")
    self.assertTrue(tdd_buckets.getFreqOfChargeRanges([1022], chargeRangeReadings.ADC_10Bit) == "15-15, 1\n")
    self.assertTrue(tdd_buckets.getFreqOfChargeRanges([1022,1023], chargeRangeReadings.ADC_10Bit) == "15-15, 1\n")#ignore error readings
    self.assertTrue(tdd_buckets.getFreqOfChargeRanges([0,100,150,300,500,70,1500,700,600,2000,1022], chargeRangeReadings.ADC_10Bit) == "0-0, 1\n3-3, 1\n6-6, 2\n11-13, 3\n15-15, 2\n")

    
unittest.main()
