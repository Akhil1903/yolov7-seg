import os
import json



label_dict = {'Valve' : 0}
width = 2560
height = 1120


def convert_json_to_txt(data):
    txt_data = ''
    for i in range(len(data['shapes'])):
        label = data['shapes'][i]['label']
        label_int = label_dict[label]
        txt_data += str(label_int) + ' '
        points = data['shapes'][i]['points']
        for point in points:
            if points.index(point) != len(points) - 1:
                txt_data += str(round(float(point[0]/width), 5)) + ' ' + str(round(float(point[1]/height), 5)) + ' '
            else:
                txt_data += str(round(float(point[0]/width), 5)) + ' ' + str(round(float(point[1]/height), 5))
        txt_data += '\n'
    return txt_data

if __name__ == '__main__':
	path = './Training_Set2_mask'
	out_path = './Training_Set3_YOLO'
	files = os.listdir(path)
	for file in files:
		if str(file).endswith('json'):
			f = open(path + '\\' + file)
			print(str(file[:-5]))
			data = json.load(f)
			txt_data = convert_json_to_txt(data)
			f.close()
			g = open(out_path + '\\' + str(file[:-5]) + '.txt', 'w')
			g.write(txt_data)
			g.close()
