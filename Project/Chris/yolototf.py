from yoloparser import YoloParser

weights_path = "./Chris/backup/newyolo_final.weights"
cfg_path = "./Chris/newyolo.cfg"
out_path = "./yolov3/yolov3.ckpt"

parser = YoloParser(cfg_path, weights_path, out_path)
parser.run()