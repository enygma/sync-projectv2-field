from github_projectv2.project import Project
import os

org = os.getenv('GITHUB_ORG')
token = os.getenv('GITHUB_API_TOKEN')
project_id = os.getenv('PROJECT_ID')
sync_field = os.getenv('SYNC_FIELD')
item_property = os.getenv('ITEM_PROPERTY')

project = Project()
project.get(org, project_id)
print('Project: %s' % project.title)

# Make sure the project has the field we want
field = None
for field in project.fields:
    if field.name == sync_field:
        print(field.name, field.id)
        break

if field is None:
    print('Field "%s" not found' % sync_field)
    exit()

print('TYPE: %s' % field.dataType)

# Now that we have the field, update the value for it

items = project.get_items()
for item in items:
    print('Item title: %s' % item.title)
    item.update_field_value(project, field, getattr(item, item_property))