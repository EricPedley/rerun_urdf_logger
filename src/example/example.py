from pathlib import Path
from rerun_urdf_logger.rerun_urdf_logger import URDFLogger
import numpy as np
import rerun as rr

if __name__ == "__main__":
    rr.init("rerun_urdf_logger_example", spawn=True)
    this_file_path = Path(__file__).resolve()
    urdf_path  = str(this_file_path.parent / "kbot" / "robot.urdf")

    logger = URDFLogger(urdf_path)
    for _ in range(100):
        config = {k: np.random.random() for k in logger.joint_names}
        logger.log(config)