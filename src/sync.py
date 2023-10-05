from github_projectv2.project import Project
import os

org = os.getenv('ORG')
token = os.getenv('GITHUB_API_TOKEN')
project_id = os.getenv('PROJECT_ID')
sync_field = os.getenv('SYNC_FIELD')
item_property = os.getenv('ITEM_PROPERTY')

print('ORG: %s' % org)
print('SYNC_FIELD: %s' % sync_field)

project = Project()
project.get(org, project_id)
if project is None:
    print('Project not found')
    exit()

print('Project: %s' % project.title)

# Make sure the project has the field we want
field = None
for f in project.fields:
    print('%s > %s' % (sync_field, f.name))
    if f.name == sync_field:
        print(f.name, f.id)
        field = f
        break

if field is None:
    print('Field "%s" not found' % sync_field)
    exit()

print('TYPE: %s' % field.dataType)
print('NAME: %s' % field.name)
print('OPTIONS LENGTH: %s' % len(field.options))

# Commented for debugging
input = getattr(item, item_property)

# If the field is a SINGLE_SELECT, we need to find the option and provide that as the value to update to
if field.dataType == 'SINGLE_SELECT':
    print('is select')
    for option in field.options:
        print(option.name, input)
        if option.name == input:
            print('found: %s %s' % (option.id, option.name))
            input = option
            break

# Now that we have the field, update the value for it
items = project.get_items()
for item in items:
    print('Item title: %s' % item.title)
    item.update_field_value(project, field, input)