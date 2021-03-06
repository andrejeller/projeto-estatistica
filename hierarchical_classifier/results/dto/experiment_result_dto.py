
class ExperimentResultDTO():

    def __init__(self, result_metrics, per_class_metrics, conf_matrix, resampling_strategy, resampling_algorithm, fold):
        self.result_metrics = result_metrics
        self.per_class_metrics = per_class_metrics
        self.conf_matrix = conf_matrix
        self.resampling_strategy = resampling_strategy
        self.resampling_algorithm = resampling_algorithm
        self.fold = fold