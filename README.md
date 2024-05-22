# Final-Backend

# API Endpoints Documentation

# User Endpoints

| Verbo   | URI                   | Descripción       |
|---------|-----------------------|-------------------|
| GET     | /api/v1/user/         | Obtener todos los usuarios |
| GET     | /api/v1/user/{id}     | Obtener un usuario por ID  |
| DELETE  | /api/v1/user/{id}     | Eliminar un usuario       |
| PUT     | /api/v1/user{id}      | Actualizar un usuario     |

#Auth Authentication

| Verbo   | URI                        | Descripción        |
|---------|----------------------------|--------------------|
| POST    | /api/v1/auth/register      | Registrar usuario  |

# Department  Endpoints

| Verbo   | URI                         | Descripción                 |
|---------|-----------------------------|-----------------------------|
| GET     | /api/v1/department/         | Obtener todos los departamentos |
| POST    | /api/v1/department/         | Crear un departamento        |
| GET     | /api/v1/department/{id}     | Obtener un departamento por ID |
| DELETE  | /api/v1/department/{id}     | Eliminar un departamento     |
| PUT     | /api/v1/department{id}      | Actualizar un departamento   |

# City Handling Endpoints

| Verbo   | URI                    | Descripción           |
|---------|------------------------|-----------------------|
| GET     | /api/v1/city/          | Obtener todas las ciudades |
| POST    | /api/v1/city/          | Crear una ciudad      |
| GET     | /api/v1/city/{id}      | Obtener una ciudad por ID |
| DELETE  | /api/v1/city/{id}      | Eliminar una ciudad   |
| PUT     | /api/v1/city{id}       | Actualizar una ciudad |

# Company  Endpoints

| Verbo   | URI                      | Descripción            |
|---------|--------------------------|------------------------|
| GET     | /api/v1/company/         | Obtener todas las compañías |
| POST    | /api/v1/company/         | Crear una compañía     |
| GET     | /api/v1/company/{id}     | Obtener una compañía por ID |
| DELETE  | /api/v1/company/{id}     | Eliminar una compañía  |
| PUT     | /api/v1/company{id}      | Actualizar una compañía |

# Branch  Endpoints

| Verbo   | URI                     | Descripción            |
|---------|-------------------------|------------------------|
| GET     | /api/v1/branch/         | Obtener todas las sucursales |
| POST    | /api/v1/branch/         | Crear una sucursal     |
| GET     | /api/v1/branch/{id}     | Obtener una sucursal por ID |
| DELETE  | /api/v1/branch/{id}     | Eliminar una sucursal  |
| PUT     | /api/v1/branch{id}      | Actualizar una sucursal |

# Client  Endpoints

| Verbo   | URI                     | Descripción          |
|---------|-------------------------|----------------------|
| GET     | /api/v1/client/         | Obtener todos los clientes |
| POST    | /api/v1/client/         | Crear un cliente     |
| GET     | /api/v1/client/{id}     | Obtener un cliente por ID |
| DELETE  | /api/v1/client/{id}     | Eliminar un cliente  |
| PUT     | /api/v1/client{id}      | Actualizar un cliente |

# Bill  Endpoints

| Verbo   | URI                   | Descripción       |
|---------|-----------------------|-------------------|
| GET     | /api/v1/bill/         | Obtener todas las facturas |
| POST    | /api/v1/bill/         | Crear una factura |
| GET     | /api/v1/bill/{id}     | Obtener una factura por ID |
| DELETE  | /api/v1/bill/{id}     | Eliminar una factura |
| PUT     | /api/v1/bill{id}      | Actualizar una factura |

# Role  Endpoints

| Verbo   | URI                   | Descripción       |
|---------|-----------------------|-------------------|
| GET     | /api/v1/rol/          | Obtener todos los roles |
| POST    | /api/v1/rol/          | Crear un rol      |
| GET     | /api/v1/rol/{id}      | Obtener un rol por ID |
| DELETE  | /api/v1/rol/{id}      | Eliminar un rol   |
| PUT     | /api/v1/rol{id}       | Actualizar un rol |

# Product  Endpoints

| Verbo   | URI                      | Descripción           |
|---------|--------------------------|-----------------------|
| GET     | /api/v1/product/         | Obtener todos los productos |
| POST    | /api/v1/product/         | Crear un producto     |
| GET     | /api/v1/product/{id}     | Obtener un producto por ID |
| DELETE  | /api/v1/product/{id}     | Eliminar un producto  |
| PUT     | /api/v1/product{id}      | Actualizar un producto |

# Category  Endpoints

| Verbo   | URI                        | Descripción           |
|---------|----------------------------|-----------------------|
| GET     | /api/v1/category/          | Obtener todas las categorías |
| POST    | /api/v1/category/          | Crear una categoría   |
| GET     | /api/v1/category/{id}      | Obtener una categoría por ID |
| DELETE  | /api/v1/category/{id}      | Eliminar una categoría |
| PUT     | /api/v1/category{id}       | Actualizar una categoría |

# Supplier  Endpoints

| Verbo   | URI                       | Descripción           |
|---------|---------------------------|-----------------------|
| GET     | /api/v1/supplier/         | Obtener todos los proveedores |
| POST    | /api/v1/supplier/         | Crear un proveedor    |
| GET     | /api/v1/supplier/{id}     | Obtener un proveedor por ID |
| DELETE  | /api/v1/supplier/{id}     | Eliminar un proveedor |
| PUT     | /api/v1/supplier{id}      | Actualizar un proveedor |

# ProductXSupplier  Endpoints

| Verbo   | URI                             | Descripción                 |
|---------|---------------------------------|-----------------------------|
| GET     | /api/v1/productxsupplier/       | Obtener todos los productos por proveedor |
| POST    | /api/v1/productxsupplier/       | Crear un producto por proveedor |
| GET     | /api/v1/productxsupplier/{id}   | Obtener un producto por proveedor por ID |
| DELETE  | /api/v1/productxsupplier/{id}   | Eliminar un producto por proveedor |
| PUT     | /api/v1/productxsupplier{id}    | Actualizar un producto por proveedor |

# SupplierXBranch  Endpoints

| Verbo   | URI                          | Descripción           |
|---------|------------------------------|-----------------------|
| GET     | /api/v1/supplierxbranch/     | Obtener todos los proveedores por sucursal |
| POST    | /api/v1/supplierxbranch/     | Crear un proveedor por sucursal |
| GET     | /api/v1/supplierxbranch/{id} | Obtener un proveedor por sucursal por ID |
| DELETE  | /api/v1/supplierxbranch/{id} | Eliminar un proveedor por sucursal |
| PUT     | /api/v1/supplierxbranch{id}  | Actualizar un proveedor por sucursal |

# Sale  Endpoints

| Verbo   | URI                   | Descripción       |
|---------|-----------------------|-------------------|
| GET     | /api/v1/sale/         | Obtener todas las ventas |
| POST    | /api/v1/sale/         | Crear una venta   |
| GET     | /api/v1/sale/{id}     | Obtener una venta por ID |
| DELETE  | /api/v1/sale/{id}     | Eliminar una venta |
| PUT     | /api/v1/sale{id}      | Actualizar una venta |

# Part  Endpoints

| Verbo   | URI                   | Descripción       |
|---------|-----------------------|-------------------|
| GET     | /api/v1/part/         | Obtener todas las partes |
| POST    | /api/v1/part/         | Crear una parte   |
| GET     | /api/v1/part/{id}     | Obtener una parte por ID |
| DELETE  | /api/v1/part/{id}     | Eliminar una parte |
| PUT     | /api/v1/part{id}      | Actualizar una parte |

# SupplierXPart  Endpoints

| Verbo   | URI                        | Descripción           |
|---------|----------------------------|-----------------------|
| GET     | /api/v1/supplierxpart/     | Obtener todos los proveedores por parte |
| POST    | /api/v1/supplierxpart/     | Crear un proveedor por parte |
| GET     | /api/v1/supplierxpart


