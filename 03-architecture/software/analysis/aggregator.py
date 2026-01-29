import statistics
from typing import List
from ..api.metrics import SimulationMetrics

class MonteCarloAggregator:
    @staticmethod
    def aggregate_runs(results: List[SimulationMetrics]) -> dict:
        """
        Aggregate results from multiple simulation runs into a statistical summary.
        """
        if not results:
            return {}

        metrics_summary = {
            "mean_pd": statistics.mean([r.prob_detection for r in results]),
            "mean_pk": statistics.mean([r.prob_kill for r in results]),
            "stdev_pd": statistics.stdev([r.prob_detection for r in results]) if len(results) > 1 else 0,
            "mean_time_to_detect": statistics.mean([r.mean_time_to_detect for r in results]),
            "mean_time_to_neutralize": statistics.mean([r.mean_time_to_neutralize for r in results]),
            "total_false_alarms": sum([r.false_alarms for r in results]),
            "sample_size": len(results)
        }

        # Confidence Interval Calculation (Simplified 95%)
        # For a more production environment, use scipy.stats
        metrics_summary["pd_95_ci"] = (
            metrics_summary["mean_pd"] - (1.96 * metrics_summary["stdev_pd"] / (len(results)**0.5)),
            metrics_summary["mean_pd"] + (1.96 * metrics_summary["stdev_pd"] / (len(results)**0.5))
        )

        return metrics_summary
