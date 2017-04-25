import numpy as np
import sketch3D
import texture
import sys, getopt

def main(argv):
	params = {}
	try:
		opts, args = getopt.getopt(argv,"hs:w:r:t:",["textureSize=","windowSize=","randomTextureSize="])
	except getopt.GetoptError:
		print 'learn.py -s <textureSize> -w <windowSize> -r <randomTextureSize> -t <textureFile>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'test.py -s <textureSize> -w <windowSize> -r <randomTextureSize> -t <textureFile>'
			sys.exit()
		elif opt in ("-s", "--textureSize"):
			params.update({'t_size':int(arg)})
		elif opt in ("-w", "--windowSize"):
			params.update({'window_size':int(arg)})
		elif opt in ("-r", "--randomTextureSize"):
			params.update({'random_texture_size':int(arg)})
		elif opt in ("-t", "--textureFile"):
			params.update({'pTexture':texture.load(arg)})
		

	mtexture = sketch3D.sketch(**params)

if __name__ == "__main__":
   main(sys.argv[1:])




