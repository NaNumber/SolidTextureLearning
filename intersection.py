
import numpy as np
from math import cos, sin, radians
from random import randint
from random import uniform
import rock

def intersect(e1, e2):
	T_e1 = np.array([[1, 0, 0, e1.center[0]],
				     [0, 1, 0, e1.center[1]],
					 [0, 0, 1, e1.center[2]],
					 [0, 0, 0, 1]])

	S_e1 = np.array([[e1.radius[0], 0, 0, 0],
					 [0,	e1.radius[1], 0, 0],
					 [0, 0, e1.radius[2], 0],
					 [0, 0, 0, 1]])

	R_x_e1 = np.array([[1, 0, 0, 0],
					   [0, cos(radians(e1.rotation[0])), sin(radians(e1.rotation[0])), 0],
					   [0,-sin(radians(e1.rotation[0])), cos(radians(e1.rotation[0])), 0],
					   [0, 0, 0, 1]])

	R_y_e1 = np.array([[cos(radians(e1.rotation[1])), 0, -sin(radians(e1.rotation[1])), 0],
					   [0, 1, 0, 0],
					   [sin(radians(e1.rotation[1])), 0, cos(radians(e1.rotation[1])),  0],
					   [0, 0, 0, 1]])

	R_z_e1 = np.array([[cos(radians(e1.rotation[2])) , sin(radians(e1.rotation[2])), 0, 0],
					   [-sin(radians(e1.rotation[2])), cos(radians(e1.rotation[2])), 0, 0],
					   [0, 0, 1, 0],
					   [0, 0, 0, 1]])

	R_e1 = np.dot(np.dot(R_x_e1, R_y_e1),R_z_e1)

	T_e1_inv = np.linalg.inv(T_e1)
	S_e1_inv = np.linalg.inv(S_e1)
	R_e1_inv = np.linalg.inv(R_e1)


	T_e2 = np.array([[1, 0, 0, e2.center[0]],
					 [0, 1, 0, e2.center[1]],
					 [0, 0, 1, e2.center[2]],
				     [0, 0, 0, 			1]])

	S_e2 = np.array([[e2.radius[0], 0, 0, 0],
					 [0, e2.radius[1], 0, 0],
					 [0, 0, e2.radius[2], 0],
					 [0, 0, 0, 1]])

	R_x_e2 = np.array([[1, 0, 0, 0],
					   [0, cos(radians(e2.rotation[0])), sin(radians(e2.rotation[0])), 0],
					   [0,-sin(radians(e2.rotation[0])), cos(radians(e2.rotation[0])), 0],
					   [0, 0, 0, 1]])

	R_y_e2 = np.array([[cos(radians(e2.rotation[1])), 0, -sin(radians(e2.rotation[1])), 0],
					   [0, 1, 0, 0],
					   [sin(radians(e2.rotation[1])), 0, cos(radians(e2.rotation[1])),  0],
					   [0, 0, 0, 1]])

	R_z_e2 = np.array([[cos(radians(e2.rotation[2])) , sin(radians(e2.rotation[2])), 0, 0],
					   [-sin(radians(e2.rotation[2])), cos(radians(e2.rotation[2])), 0, 0],
					   [0, 0, 1, 0],
					   [0, 0, 0, 1]])

	R_e2 = np.dot(np.dot(R_x_e2, R_y_e2), R_z_e2)

	T_e2_inv = np.linalg.inv(T_e2)
	S_e2_inv = np.linalg.inv(S_e2)
	R_e2_inv = np.linalg.inv(R_e2)

	p_e2space = np.array([0.25, 0.4330127019, 0.8660254038, 1.])

	for i in range(150):
		dp_du_e2space = np.array([p_e2space[2],0,-p_e2space[0]])
		dp_du_e2space = dp_du_e2space/np.linalg.norm(dp_du_e2space)
		dp_du_e2space = np.append(dp_du_e2space, 1)
		dp_dv_e2space = np.array([0, p_e2space[2], -p_e2space[1]])
		dp_dv_e2space = dp_dv_e2space/np.linalg.norm(dp_dv_e2space)
		dp_dv_e2space = np.append(dp_dv_e2space, 1)
		
		dp2_du_dv_e2space = np.append(-p_e2space[:3], 1)

		p_global = np.dot(np.dot(np.dot(T_e2, R_e2), S_e2), p_e2space)
		dp_du_global = np.dot(np.dot(R_e2, S_e2), dp_du_e2space)
		dp_dv_global = np.dot(np.dot(R_e2, S_e2), dp_dv_e2space)
		dp2_du_dv_global = np.dot(np.dot(R_e2, S_e2), dp2_du_dv_e2space)

		p_e1space = np.dot(np.dot(np.dot(S_e1_inv, R_e1_inv), T_e1_inv), p_global)
		dp_du_e1space = np.dot(np.dot(S_e1_inv, R_e1_inv), dp_du_global)
		dp_dv_e1space = np.dot(np.dot(S_e1_inv, R_e1_inv), dp_dv_global)
		dp2_du_dv_e1space = np.dot(np.dot(S_e1_inv, R_e1_inv), dp2_du_dv_global)

		N_e1space = p_e1space[:3]/np.linalg.norm(p_e1space[:3])
		
		dd_du_e1space = np.dot(dp_du_e1space[:3], N_e1space)
		dd_dv_e1space = np.dot(dp_dv_e1space[:3], N_e1space)
		dd2_du_dv_e1space = np.dot(dp2_du_dv_e1space[:3], N_e1space)

		next_p_e1space = p_e1space[:3] - (dd_du_e1space/dd2_du_dv_e1space)*dp_du_e1space[:3] - (dd_dv_e1space/dd2_du_dv_e1space)*dp_dv_e1space[:3]

		distance_e1space = sum(next_p_e1space**2)**0.5
		print distance_e1space

		if distance_e1space <= 1:
			return True

		next_p_global = np.dot(np.dot(np.dot(T_e1, R_e1), S_e1), np.append(next_p_e1space,1))
		p_e2space = np.dot(np.dot(np.dot(S_e2_inv, R_e2_inv), T_e2_inv), next_p_global)

	return False



r1 = rock.Rock3D([0,0,0],[10,10,10],[255,0,0],[0,0,0])
r2 = rock.Rock3D([10,10,10],[10,10,10],[255,0,0],[0,0,0])

intersect(r1,r2)


	





















	








