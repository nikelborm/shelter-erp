from .tablesDefinitions import AbstractPetTable, EmployeeTable, PetInstanceTable, PetTakeoutRequestTable, ShelterTable, UserTable
from .tools import DB_CRUD_Functions


shelter_db_crud             = DB_CRUD_Functions('Shelter',           'Shelters',             ShelterTable)
user_db_crud                = DB_CRUD_Functions('User',              'Users',                UserTable)
employee_db_crud            = DB_CRUD_Functions('Employee',          'Employees',            EmployeeTable)
employee_in_shelter_db_crud = DB_CRUD_Functions('Employee',          'Employees',            EmployeeTable)
abstract_pet_db_crud        = DB_CRUD_Functions('AbstractPet',       'AbstractPets',         AbstractPetTable)
pet_instance_db_crud        = DB_CRUD_Functions('PetInstance',       'PetInstances',         PetInstanceTable)
pet_takeout_request_db_crud = DB_CRUD_Functions('PetTakeoutRequest', 'PetTakeoutRequests',   PetTakeoutRequestTable)



# shelter_db_crud
selectAllShelters = shelter_db_crud.selectAllEntities
selectShelterByPk = shelter_db_crud.selectEntityByPk
insertShelter     = shelter_db_crud.insertEntity
updateShelterByPk = shelter_db_crud.updateEntityByPk
deleteShelterByPk = shelter_db_crud.deleteEntityByPk

# user_db_crud
selectAllUsers = user_db_crud.selectAllEntities
selectUserByPk = user_db_crud.selectEntityByPk
insertUser     = user_db_crud.insertEntity
updateUserByPk = user_db_crud.updateEntityByPk
deleteUserByPk = user_db_crud.deleteEntityByPk

# employee_db_crud
selectAllEmployees = employee_db_crud.selectAllEntities
selectEmployeeByPk = employee_db_crud.selectEntityByPk
insertEmployee     = employee_db_crud.insertEntity
updateEmployeeByPk = employee_db_crud.updateEntityByPk
deleteEmployeeByPk = employee_db_crud.deleteEntityByPk

# employee_in_shelter_db_crud
selectAllEmployeeInShelters = employee_in_shelter_db_crud.selectAllEntities
selectEmployeeInShelterByPk = employee_in_shelter_db_crud.selectEntityByPk
insertEmployeeInShelter     = employee_in_shelter_db_crud.insertEntity
updateEmployeeInShelterByPk = employee_in_shelter_db_crud.updateEntityByPk
deleteEmployeeInShelterByPk = employee_in_shelter_db_crud.deleteEntityByPk

# abstract_pet_db_crud
selectAllAbstractPets = abstract_pet_db_crud.selectAllEntities
selectAbstractPetByPk = abstract_pet_db_crud.selectEntityByPk
insertAbstractPet     = abstract_pet_db_crud.insertEntity
updateAbstractPetByPk = abstract_pet_db_crud.updateEntityByPk
deleteAbstractPetByPk = abstract_pet_db_crud.deleteEntityByPk

# pet_instance_db_crud
selectAllPetInstances = pet_instance_db_crud.selectAllEntities
selectPetInstanceByPk = pet_instance_db_crud.selectEntityByPk
insertPetInstance     = pet_instance_db_crud.insertEntity
updatePetInstanceByPk = pet_instance_db_crud.updateEntityByPk
deletePetInstanceByPk = pet_instance_db_crud.deleteEntityByPk

# pet_takeout_request_db_crud
selectAllPetTakeoutRequests = pet_takeout_request_db_crud.selectAllEntities
selectPetTakeoutRequestByPk = pet_takeout_request_db_crud.selectEntityByPk
insertPetTakeoutRequest     = pet_takeout_request_db_crud.insertEntity
updatePetTakeoutRequestByPk = pet_takeout_request_db_crud.updateEntityByPk
deletePetTakeoutRequestByPk = pet_takeout_request_db_crud.deleteEntityByPk
