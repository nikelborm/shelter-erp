from .models import PetTakeoutRequestStatusEnum, DBPetTakeoutRequestToInsert
from .tablesDefinitions import AbstractPetTable, EmployeeUserTable, PetInstanceTable, PetTakeoutRequestTable, ShelterTable, UserTable, EmployeeUserInShelterTable, PET_TAKEOUT_REQUEST_CNS
from .tools import DB_CRUD_Functions


shelter_db_crud                  = DB_CRUD_Functions('Shelter',           'Shelters',            ShelterTable)
user_db_crud                     = DB_CRUD_Functions('User',              'Users',               UserTable)
employee_users_db_crud           = DB_CRUD_Functions('EmployeeUser',      'EmployeeUsers',       EmployeeUserTable)
employee_user_in_shelter_db_crud = DB_CRUD_Functions('EmployeeInShelter', 'EmployeesInShelters', EmployeeUserInShelterTable)
abstract_pet_db_crud             = DB_CRUD_Functions('AbstractPet',       'AbstractPets',        AbstractPetTable)
pet_instance_db_crud             = DB_CRUD_Functions('PetInstance',       'PetInstances',        PetInstanceTable)
pet_takeout_request_db_crud      = DB_CRUD_Functions('PetTakeoutRequest', 'PetTakeoutRequests',  PetTakeoutRequestTable)



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
selectAllEmployeeUsers = employee_users_db_crud.selectAllEntities
selectEmployeeUserByPk = employee_users_db_crud.selectEntityByPk
insertEmployeeUser     = employee_users_db_crud.insertEntity
updateEmployeeUserByPk = employee_users_db_crud.updateEntityByPk
deleteEmployeeUserByPk = employee_users_db_crud.deleteEntityByPk

# employee_in_shelter_db_crud
selectAllEmployeeUserInShelters = employee_user_in_shelter_db_crud.selectAllEntities
selectEmployeeUserInShelterByPk = employee_user_in_shelter_db_crud.selectEntityByPk
insertEmployeeUserInShelter     = employee_user_in_shelter_db_crud.insertEntity
updateEmployeeUserInShelterByPk = employee_user_in_shelter_db_crud.updateEntityByPk
deleteEmployeeUserInShelterByPk = employee_user_in_shelter_db_crud.deleteEntityByPk

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
