#  nomes de variaveis de TABLE's para a API

DATABASE_NAME="packDeliv_DB"

COMPANY= 'Company'
DELIVERYMAN= 'Deliveryman'
ADDRESS= 'Adress'
VEHICLE='Vehicle'
SERVICE_ORDER='Service_order'
DELIVERY='Delivery'
PACKAGE='Package'
LOCALIZATION="Localization"
CLIENT="Client"

CLIENT_ID='Id'
CLIENT_UPI='CPF'#unique client identifier
CLIENT_NAME='Nome'
ADDRESSES='Enderecos'

COMPANY_ID = 'Id'
COMPANY_ID_ADDRESS ='Id_endereco'
COMPANY_NAME='Nome_fantasia'
COMPANY_PASSWORD ='Senha'
COMPANY_LOGIN ='Login'
COMPANY_EMAIL ='Email'
COMPANY_UCI= 'CNPJ' # unique identifier of company
COMPANY_TYPE= 'Tipo'

DELIVERYMAN_ID= 'Id'
DELIVERYMAN_NAME='Nome_completo'
DELIVERYMAN_ID_VEHICLE= 'Id_veiculo'
DELIVERYMAN_ID_COMPANY = 'id_empresa'
DELIVERYMAN_NAME='Nome'
DELIVERYMAN_STATUS='Status'
DELIVERYMAN_DUI= 'CNH' #driver unique identifier
DELIVERYMAN_STATUS= 'Status'
DELIVERYMAN_READY= 'Apto'
DELIVERYMAN_LOCALIZATION= 'Localizacao'

ADDRESS_ID= 'Id'
ADDRESS_STREET= 'Logradouro'
ADDRESS_NUMBER= 'Numero'
ADDRESS_COMPLEMENT= 'Complemento'
ADDRESS_DISTRICT= 'Bairro'
ADDRESS_POSTAL_CODE = 'CEP'
ADDRESS_CITY= 'Cidade'
ADDRESS_STATE= 'Estado'
ADDRESS_COUNTRY= 'Pais'
ADDRESS_TYPE= 'Tipo'

ADDRESS_COMPANY_MATRIX='endereco_empresa_matriz'
ADDRESS_COMPANY='endereco_empresa'
ADDRESS_CLIENT='endereco_cliente'

VEHICLE_ID= 'Id'
VEHICLE_LICENSE_PLATE= 'placa'
VEHICLE_YEAR = 'ano'
VEHICLE_MODEL = 'modelo'
VEHICLE_COLOR = 'cor'
VEHICLE_READY= 'apto'
VEHICLE_VOLUME= 'volume'


SERVICE_ORDER_ID='Id'
SERVICE_ORDER_IDENTIFIER_CODE='Codigo'
SERVICE_ORDER_SHIPPING_DATE= 'Data_expedicao'
SERVICE_ORDER_FINALIZATION_DATE='Data_finalizacao'
SERVICE_ORDER_STATUS='Status'
DELIVERIES='Entregas'

DELIVERY_ID='Id'
DELIVERY_IDENTIFIER_CODE='codigo'
DELIVERY_SHIPPING_DATE='Data_expedicao'
DELIVERY_FINALIZATION_DATE='Data_finalizacao'
#!/usr/bin/python3.5

DELIVERY_ID_SERVICE_ORDER='Id_ordem_de_servico'
DELIVERY_ID_PACKAGE='Id_pacote'
DELIVERY_ID_SUCESS='Sucesso'
DELIVERY_STATUS='Status'
DELIVERY_TYPE='Tipo'

PACKAGE_ID='Id'
PACKAGE_WIDTH='Largura'
PACKAGE_HEIGHT='Altura'
PACKAGE_LENGTH='Comprimento'
PACKAGE_WEIGHT='Peso'
PACKAGE_SHIPPED='Expedido'
PACKAGE_RECEIVED='Recebido'
PACKAGE_ID_ADDRESS_START ='Id_endereco_inicio'
PACKAGE_ID_ADDRESS_DESTINY ='Id_endereco_destino'
PACKAGE_CURRENT_STATIC_LOCATION='Local_atual_estatico'
PACKAGE_STATUS='Status'
PACKAGE_VOLUME="volume"

LOCALIZATION_ID="Id"
LOCALIZATION_LAT="Lat"
LOCALIZATION_LONG="Long"
LOCALIZATION_TYPE="Tipo"

LOCALIZATION_ADDRESS="localizacao_endereco"
LOCALIZATION_DELIVERYMAN="localizacao_entregador"
