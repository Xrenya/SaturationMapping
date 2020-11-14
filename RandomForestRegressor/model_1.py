import numpy as np
import pandas as pd
import pickle
import argparse
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

RANDOM_STATE = 66

parser = argparse.ArgumentParser()
parser.add_argument(
	"--por",
	nargs="?",
	metavar="path",
	action="store",
	default="./por.txt"
)
parser.add_argument(
	"--res",
	nargs="?",
	metavar="path",
	type=str,
	default="./res.txt"
)
parser.add_argument(
	"--swat", 
	nargs="?",
	metavar="path",
	type=str,
	action="store",
	default="./swat.txt"
)
parser.add_argument(
	"--test",
	nargs="?",	
	type=bool,
	help="Start training and validation",
	default=True
)
parser.add_argument(
	"--load_model",
	nargs="?",
	metavar="path",	
	type=str,
	action="store",
	help="A path to the pickle model to test the model",
	default="rf_1.sav"
)

def main(args):
	if args.test:
		# Reading files:
		files = {
		    "porosity": args.por,
	        "resistivity": args.res,
	        "saturation": args.swat
		}
		print(files)
		data_dict = {}
		for file in files:
			with open(files[file], "r") as f:
				data_dict[file] = f.read().splitlines()
		df = pd.DataFrame(data_dict)
		df["porosity"] = pd.to_numeric(df["porosity"], errors="coerce")
		df["resistivity"] = pd.to_numeric(df["resistivity"], errors="coerce")
		df["saturation"] = pd.to_numeric(df["saturation"], errors="coerce")
		assert len(df["porosity"]) == len(df["resistivity"])
		assert len(df["resistivity"]) == len(df["saturation"])
		X = df.drop(columns=["saturation"])
		y = df["saturation"]
		X_train, X_val, y_train, y_val = train_test_split(
			X, y,
			test_size=0.2,
			random_state=RANDOM_STATE
		)
		print("Data sample:")
		print(df.sample(5))

		# Training model section
		rf = RandomForestRegressor(
			n_estimators=100,
			criterion='mse',
			random_state=RANDOM_STATE
		)
		rf_val_score = model_pipeline(rf, 
			X_train, y_train,
			X_val, y_val,
			training=True)

	# Test model section
	else:
		print("Test model")
		# Reading files:
		files = {
		    "porosity": args.por,
	        "resistivity": args.res
		}
		data_dict = {}
		for file in files:
			with open(files[file], "r") as f:
				data_dict[file] = f.read().splitlines()
		df = pd.DataFrame(data_dict)
		df["porosity"] = pd.to_numeric(df["porosity"], errors="coerce")
		df["resistivity"] = pd.to_numeric(df["resistivity"], errors="coerce")
		assert len(df["porosity"]) == len(df["resistivity"])
		X = df.drop(columns=["saturation"])
		rf_loaded = pickle.load(open(args.load_model, "rb"))
		predictions = model_pipeline(rf_loaded, X_val=X, training=False)
		df_out = pd.DataFrame({"saturation": predictions})
		df_out.to_csv("./saturation.csv", index=False)

def model_pipeline(model, 
	    X_train=None, y_train=None,
	    X_val=None, y_val=None,
	    training=True):
	pipeline = Pipeline([
		("scaler", StandardScaler()),
		("model", model)
	])
	if training:
		pipeline.fit(X_train, y_train)
		print(f"Training MSE score: {pipeline.score(X_train, y_train)}")
		filename = "./rf_1.sav"
		pickle.dump(pipeline, open(filename, "wb"))
		preds = pipeline.predict(X_val)
		model_score = mean_squared_error(y_val, preds)
		print(f"Validation MSE score: {model_score}")
		return model_score
	else:
		preds = model.predict(X_val)
		return preds

if __name__ == "__main__":
	args = parser.parse_args()
	print(args)
	main(args)
