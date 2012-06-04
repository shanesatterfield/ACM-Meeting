import sys 
import csv
import markdown

from jinja2 import Environment, PackageLoader

if __name__ == '__main__':

	def add_member(name, pos, email):
		return {
			"name" : name,
			"position" : pos,
			"email" : email
		}

	args = sys.argv[1:]
	
	env = Environment(loader=PackageLoader('qad_render', 'app/template'))
	template = env.get_template('paper.html')

	year = args[0]
	content = args[1]
	date = args[2]
	
	with open(content, 'r') as f:
		content = f.read()

	member_data = csv.reader(open('./app/data/adminlist/' + year + '.csv'))

	execs = []
	appos = []
	
	index = 0
	for row in member_data:
		if index > 1:
			admin =  row[-1] == '1' if True else False
			if admin:
				execs.append(add_member(row[0], row[1], row[2]))
			else:
				appos.append(add_member(row[0], row[1], row[2]))
		index += 1
	
	print template.render({
		"executive" : execs,
		"appointed" : appos,
		"minutes" : markdown.markdown(content)
	});
	print execs