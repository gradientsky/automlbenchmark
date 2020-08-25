import logging
import warnings

import matplotlib

from autogluon.autogluon_tooling import AutogluonRunner
from frameworks.shared.callee import call_run

matplotlib.use('agg')  # no need for tk

warnings.simplefilter("ignore")

log = logging.getLogger(__name__)

runner = AutogluonRunner()

if __name__ == '__main__':
    call_run(runner.run)
