from src.config.tables_column_names import AbstractPetTable, EmployeeTable, PetInstanceTable, PetTakeoutRequestTable, ShelterTable, UserTable
from src.tools import DB_CRUD_Functions


shelter_db_crud             = DB_CRUD_Functions('Shelter',           'Shelters',             ShelterTable)
user_db_crud                = DB_CRUD_Functions('User',              'Users',                UserTable)
employee_db_crud            = DB_CRUD_Functions('Employee',          'Employees',            EmployeeTable)
employee_in_shelter_db_crud = DB_CRUD_Functions('Employee',          'Employees',            EmployeeTable)
abstract_pet_db_crud        = DB_CRUD_Functions('AbstractPet',       'AbstractPets',         AbstractPetTable)
pet_instance_db_crud        = DB_CRUD_Functions('PetInstance',       'PetInstances',         PetInstanceTable)
pet_takeout_request_db_crud = DB_CRUD_Functions('PetTakeoutRequest', 'PetTakeoutRequests',   PetTakeoutRequestTable)



# shelter_db_crud
selectAllShelters = shelter_db_crud.selectAllEntities
selectShelterById = shelter_db_crud.selectEntityByPk
insertShelter     = shelter_db_crud.insertEntity
updateShelterById = shelter_db_crud.updateEntityByPk
deleteShelterById = shelter_db_crud.deleteEntityByPk

# user_db_crud
selectAllUsers = user_db_crud.selectAllEntities
selectUserById = user_db_crud.selectEntityByPk
insertUser     = user_db_crud.insertEntity
updateUserById = user_db_crud.updateEntityByPk
deleteUserById = user_db_crud.deleteEntityByPk

# employee_db_crud
selectAllEmployees = employee_db_crud.selectAllEntities
selectEmployeeById = employee_db_crud.selectEntityByPk
insertEmployee     = employee_db_crud.insertEntity
updateEmployeeById = employee_db_crud.updateEntityByPk
deleteEmployeeById = employee_db_crud.deleteEntityByPk

# employee_in_shelter_db_crud
selectAllEmployeeInShelters = employee_in_shelter_db_crud.selectAllEntities
selectEmployeeInShelterByPk = employee_in_shelter_db_crud.selectEntityByPk
insertEmployeeInShelter     = employee_in_shelter_db_crud.insertEntity
updateEmployeeInShelterByPk = employee_in_shelter_db_crud.updateEntityByPk
deleteEmployeeInShelterByPk = employee_in_shelter_db_crud.deleteEntityByPk

# abstract_pet_db_crud
selectAllAbstractPets = abstract_pet_db_crud.selectAllEntities
selectAbstractPetById = abstract_pet_db_crud.selectEntityByPk
insertAbstractPet     = abstract_pet_db_crud.insertEntity
updateAbstractPetById = abstract_pet_db_crud.updateEntityByPk
deleteAbstractPetById = abstract_pet_db_crud.deleteEntityByPk

# pet_instance_db_crud
selectAllPetInstances = pet_instance_db_crud.selectAllEntities
selectPetInstanceById = pet_instance_db_crud.selectEntityByPk
insertPetInstance     = pet_instance_db_crud.insertEntity
updatePetInstanceById = pet_instance_db_crud.updateEntityByPk
deletePetInstanceById = pet_instance_db_crud.deleteEntityByPk

# pet_takeout_request_db_crud
selectAllPetTakeoutRequests = pet_takeout_request_db_crud.selectAllEntities
selectPetTakeoutRequestById = pet_takeout_request_db_crud.selectEntityByPk
insertPetTakeoutRequest     = pet_takeout_request_db_crud.insertEntity
updatePetTakeoutRequestById = pet_takeout_request_db_crud.updateEntityByPk
deletePetTakeoutRequestById = pet_takeout_request_db_crud.deleteEntityByPk
