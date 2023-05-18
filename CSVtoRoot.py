# -*- coding: utf-8 -*-
'''
Author: U. Guney Tok

Description: Dark current of the PMTs from ZDC's RPD detectors.

Script usage: python CSVtoRoot.py --region
		e.g   python CSVtoRoot.py Plus
'''

import ROOT
import sys
import os

fileNames_Minus=["ZDC_Minus/RPD_M_csvFiles/230512_A1_Ch1.csv","ZDC_Minus/RPD_M_csvFiles/230512_A1_Ch2.csv","ZDC_Minus/RPD_M_csvFiles/230512_A1_Ch3.csv","ZDC_Minus/RPD_M_csvFiles/230512_A1_Ch4.csv","ZDC_Minus/RPD_M_csvFiles/230512_A2_Ch5.csv","ZDC_Minus/RPD_M_csvFiles/230512_A2_Ch6.csv","ZDC_Minus/RPD_M_csvFiles/230512_A2_Ch7.csv","ZDC_Minus/RPD_M_csvFiles/230512_A2_Ch8.csv","ZDC_Minus/RPD_M_csvFiles/230512_B3_Ch9.csv","ZDC_Minus/RPD_M_csvFiles/230512_B3_Ch10.csv","ZDC_Minus/RPD_M_csvFiles/230512_B3_Ch11.csv","ZDC_Minus/RPD_M_csvFiles/230512_B3_Ch12.csv","ZDC_Minus/RPD_M_csvFiles/230512_B4_Ch13.csv","ZDC_Minus/RPD_M_csvFiles/230512_B4_Ch14.csv","ZDC_Minus/RPD_M_csvFiles/230512_B4_Ch15.csv","ZDC_Minus/RPD_M_csvFiles/230512_B4_Ch16.csv"]

fileNames_Plus=["ZDC_Plus/RPD_P_csvFiles/230511_D1_Ch1.csv","ZDC_Plus/RPD_P_csvFiles/230511_D1_Ch2.csv","ZDC_Plus/RPD_P_csvFiles/230511_D1_Ch3.csv","ZDC_Plus/RPD_P_csvFiles/230511_D1_Ch4.csv","ZDC_Plus/RPD_P_csvFiles/230511_D2_Ch5.csv","ZDC_Plus/RPD_P_csvFiles/230511_D2_Ch6.csv","ZDC_Plus/RPD_P_csvFiles/230511_D2_Ch7.csv","ZDC_Plus/RPD_P_csvFiles/230511_D2_Ch8.csv","ZDC_Plus/RPD_P_csvFiles/230511_C3_Ch9.csv","ZDC_Plus/RPD_P_csvFiles/230511_C3_Ch10.csv","ZDC_Plus/RPD_P_csvFiles/230511_C3_Ch11.csv","ZDC_Plus/RPD_P_csvFiles/230511_C3_Ch12.csv","ZDC_Plus/RPD_P_csvFiles/230512_C4_CH13_HV11ON.csv","ZDC_Plus/RPD_P_csvFiles/230512_C4_CH14_HV11ON.csv","ZDC_Plus/RPD_P_csvFiles/230512_C4_CH15_HV11ON.csv","ZDC_Plus/RPD_P_csvFiles/230512_C4_CH16_HV110N.csv"]

region = sys.argv[1]

#fileNames=["ZDC_Minus/RPD_M_csvFiles/230512_A2_Ch7.csv"]

snapshotOptions = ROOT.RDF.RSnapshotOptions()
snapshotOptions.fMode  = "RECREATE"
snapshotOptions.fOverwriteIfExists = True

count = 0

if region == "Plus":
	fileNames = fileNames_Plus
elif region == "Minus":
	fileNames = fileNames_Minus

for fileName in fileNames:
	count = count +1
	
	df = ROOT.RDF.MakeCsvDataFrame(fileName)

	#rootfileName = "RPDM_Channel_%s.root"%str(count)
	rootfileName = "RPD_%s.root"%region
	treeName = "Channel_%s"%str(count)

	histo1D = df.Histo1D(("dark current","ZDC_RPD %s; Time;Voltage"%region,250,-125,125),"Voltage")

	df.Snapshot(treeName,rootfileName,"",snapshotOptions)
	f = ROOT.TFile.Open(rootfileName)
	c = ROOT.TCanvas()
	#c.SetLogx()
	c.SetLogy()
	histo1D.Draw()
	c.SaveAs("ZDC_%s/Histograms/RPD%s_Channel_%s.png"%(region,region,str(count)))

