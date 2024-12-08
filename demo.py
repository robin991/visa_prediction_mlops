from us_visa.pipline.training_pipeline import TrainPipeline
import numpy as  np
np.float_ = np.float64

obj = TrainPipeline()
obj.run_pipeline()