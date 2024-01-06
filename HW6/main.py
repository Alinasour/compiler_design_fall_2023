import os
import sys
os.add_dll_directory("C:\\Program Files\\SciTools\\bin\\pc-win64\\")
sys.path.append("C:\\Program Files\\SciTools\\bin\\pc-win64\\python")
import understand as und

db=und.open("C:\\Users\\USER\\OpenUnderstand\\OpenUnderstand.udb")

if not db:
    print("Failed to open the Understand database.")
    sys.exit(1)

# Get all class entities
'''class_entities = db.ents()

# Iterate through class entities and print their names
n=0
for class_entity in class_entities:
    #print("Class Name:", class_entity.name())
    n+=1
print(n)
# Close the Understand database
db.close()'''

def get_references_info(db):
    # Initialize a list to store references information
    references_info = []

    # Query all entities in the database
    query = db.ents()

    # Iterate through each entity in the query result
    for ent in query:
        # Iterate through references of the entity with the type 'create_createby' or 'create'
        for ref in ent.refs('Couple, Coupleby'):
            if ref.kindname() == 'Implicit Extend':
                continue
            # Get information about the reference
            reference_kind = ref.kindname()
            entity_performing_reference = ent.name()
            entity_being_referenced = ref.ent().name()

            # Append information to the list
            references_info.append({
                'Reference kind': reference_kind,
                'Entity performing references': entity_performing_reference,
                'Entity being referenced': entity_being_referenced
            })

    return references_info


# Open the Understand database
db_path = "C:\\Users\\USER\\java 8 project\\java 8 project.udb"
db = und.open(db_path)

if not db:
    print("Failed to open the Understand database.")
    sys.exit(1)

# Get references information
references_info = get_references_info(db)

# Close the Understand database
db.close()

# Print the header
print(f"{'Reference kind':<20}{'Entity performing references':<20}{'Entity being referenced':<20}")

# Print each row of the references information
for info in references_info:
    #if info['Reference kind'] == "Create":
    print(f"{info['Reference kind']:<20}{info['Entity performing references']:<20}{info['Entity being referenced']:<20}")

