__all__ = [
    'AutoQuality',
    'DEFAULT_DISTRIBUTIONS',
]
import pandas
import toloka.autoquality.scoring
import toloka.client
import toloka.client.filter
import toloka.client.pool
import toloka.client.task
import typing


def _create_autoquality_pool_default(
    autoquality: 'AutoQuality',
    params: typing.Dict[str, typing.Any],
    private_name: str
): ...


DEFAULT_DISTRIBUTIONS = ...

class AutoQuality:
    """This class implements a tool to help set up quality control for Toloka project.
    To use `toloka.autoquality` install toloka-kit via `pip install toloka-kit[autoquality]`

    Attributes:
        toloka_client: TolokaClient instance to interact with requester's account
        project_id: Toloka project ID
        base_pool_id: Template Pool for autoquality pools
        training_pool_id:  Training Pool ID
        exam_pool_id: Exam Pool ID
        exam_skill_id: Skill for filtering by exam perfomance
        label_field: Output field name
        n_iter: Number of an autoquality pools
        parameter_distributions: Parameter distributions
        score_func: Callable to calculate pool scores
        ranking_func: Callabale to ranking pools based on their scores
        create_autoquality_pool_func: Callable to create autoquality pool
        run_id: ID of autoquality run

    Example:
        >>> aq = AutoQuality(
        >>>   toloka_client=toloka_client,
        >>>   project_id=...,
        >>>   base_pool_id=...,
        >>>   training_pool_id=...,
        >>>   exam_pool_id = ...,
        >>>   exam_skill_id = ...
        >>> )
        >>> aq.setup_pools()
        >>> aq.create_tasks(aq_tasks)
        >>> aq.run()
        >>> aq.best_pool_params
    """

    def setup_pools(self):
        """Create autoquality pools with sampled quality control parameters.
        """
        ...

    def create_tasks(self, tasks: typing.List[toloka.client.task.Task]):
        """Add tasks to autoquality pools.
        If the GoldenSet rule is used in quality control then control tasks should also be provided.
        """
        ...

    def run(self):
        """Run autoquality process.
        """
        ...

    def archive_autoquality_pools(self):
        """Archive all pools created by `AutoQuality.setup_pools`
        """
        ...

    def __init__(
        self,
        toloka_client: toloka.client.TolokaClient,
        project_id: str,
        base_pool_id: str,
        training_pool_id: str,
        exam_pool_id: typing.Optional[str] = None,
        exam_skill_id: typing.Optional[str] = None,
        label_field: str = 'label',
        n_iter: int = 10,
        parameter_distributions: typing.Dict = ...,
        score_func: typing.Callable = toloka.autoquality.scoring.default_calc_scores,
        ranking_func: typing.Callable = toloka.autoquality.scoring.default_calc_ranks,
        create_autoquality_pool_func: typing.Callable = _create_autoquality_pool_default,
        run_id: str = 'AutoQuality Project 2022-09-16 13:02:18'
    ) -> None:
        """Method generated by attrs for class AutoQuality.
        """
        ...

    toloka_client: toloka.client.TolokaClient
    project_id: str
    base_pool_id: str
    training_pool_id: str
    exam_pool_id: typing.Optional[str]
    exam_skill_id: typing.Optional[str]
    label_field: str
    n_iter: int
    parameter_distributions: typing.Dict
    score_func: typing.Callable
    ranking_func: typing.Callable
    create_autoquality_pool_func: typing.Callable
    run_id: str
    autoquality_pools: typing.List[toloka.client.pool.Pool]
    autoquality_pool_skills: typing.Dict[str, toloka.client.filter.Skill]
    worker_autoquality_pool_skills: typing.Dict[str, str]
    params: typing.Dict[str, typing.Dict[str, typing.Any]]
    _base_pool: typing.Optional[toloka.client.pool.Pool]
    _assigned_workers: typing.Dict[str, str]
    _scores: typing.Optional[typing.Dict[str, typing.Any]]
    _ranks: typing.Optional[pandas.DataFrame]
    _pruned_params: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]
