import datetime, json, ast, os.path, numpy as np, pandas as pd, time as ti, matplotlib.pyplot as plt
from datetime import time, timedelta
from NRInsightsQuery import NRInsightsQuery

class HistogramIntersection:
	histoIntersectionDictionary = {}
	def __init__(self):
		with open('config.json', 'r') as json_data_file:
			self.config = json.load(json_data_file)

	def calcHistogramIntersection(self, h1, h2):
		normalH1 = self.normalizedHisto(ast.literal_eval(h1))
		normalH2 = self.normalizedHisto(ast.literal_eval(h2))
		sm = 0
		for i in range(len(normalH1)):
			sm += (min(normalH1[i], normalH2[i]))
		return sm

	def normalizedHisto(self, histo):
		return [float(i)/sum(histo) for i in histo]

	def collectData(self):
		try:
			NRObj = NRInsightsQuery()
			if os.path.exists(self.config['filename']):
				df = pd.read_csv(self.config['filename'])
			else:
				df = pd.DataFrame(index=self.config['emptyDFIndex'])
			for i in range(self.config['numPrevDays']):
				fromDay = str((datetime.datetime.today() - timedelta(i+1)).date())
				for i in range(self.config['numDayHours']):
					if fromDay in df.columns:
						if df[fromDay][i]:
							continue
					fromTime = str(i).zfill(2) + ":"  + "00:00"
					toTime = str(i+1).zfill(2) + ":" + "00:00"
					if toTime == "24:00:00":
						toTime = "23:59:59"
					fromDT =  "'" + fromDay + " " + fromTime + "-0500" +"'"
					toDT = "'" + fromDay + " " + toTime + "-0500" +"'"
					query = str(NRObj.getBackendDurationQuery(fromDT, toDT))
					jsonData = (NRObj.queryInsights(query)).json()
					for retry in range(self.config['retryLimit']):
						if 'error' not in jsonData:
							histoData = jsonData['results'][0]['histogram']
							break
					if histoData:
						if fromDay not in df:
							df.insert(0, fromDay, "")
						df[fromDay][i] = histoData
					ti.sleep(self.config['sleepSeconds'])
			df.to_csv(self.config['filename'])
			return df
		except (KeyboardInterrupt, SystemExit):
			raise

	def cleanUnNamedData(self, df):
		for column in df.columns:
			if 'Unnamed' in column:
				del df[column]
		df.reindex_axis(sorted(df.columns), axis=1)
		df.to_csv(self.config['filename'])

	def runDataThruIntersection(self, df):
		stepSize = self.config['stepSize']
		index=0
		row=0
		col=0
		numCols = len(df.columns)
		numRows = len(df.index)
		while(col< numCols):
			prevRow = row
			prevCol = col
			h1 = df.ix[row][col]
			index += stepSize
			row = ((index-1)%numRows)
			col = ((index-1)/numRows)
			if(col<numCols):
				h2 = df.ix[row][col]
				histoIntFactor = round(self.calcHistogramIntersection(h1,h2),2)
				self.histoIntersectionDictionary[str(df.columns[prevCol]) + ":" + str(df.index[prevRow]).zfill(2) + ":"  + "00:00"] = histoIntFactor

		self.plotHistoIntersection(self.histoIntersectionDictionary)

	def plotHistoIntersection(self, D):
		for key in sorted(D.iterkeys()):
			if D[key] < 0.99:
				print "%s: %s" % (key, D[key])
		plt.bar(range(len(D)), D.values(), align='center')
		plt.xticks(range(len(D)), D.keys())
		plt.show()			


def main():
	histObj = HistogramIntersection()
	dataFrame = histObj.collectData()
	histObj.cleanUnNamedData(dataFrame)
	histObj.runDataThruIntersection(dataFrame)


if __name__ == "__main__":
    main()

