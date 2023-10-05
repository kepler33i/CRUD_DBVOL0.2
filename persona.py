class Persona:
    def __init__(self, nombre_apellido, rut, fecha_nacimiento, direccion, telefono, correo_electronico, genero, estado_civil, ocupacion, informacion_adicional):
        self.nombre_apellido = nombre_apellido
        self.rut = rut
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.telefono = telefono
        self.correo_electronico = correo_electronico
        self.genero = genero
        self.estado_civil = estado_civil
        self.ocupacion = ocupacion
        self.informacion_adicional = informacion_adicional
        

    # @property
    # def cuenta_bancaria(self):
    #     return "****" + self._cuenta_bancaria[-4:]
    
    def to_dict(self):
        return {
            "nombre": self.nombre_apellido,
            "rut": self.rut,
            "fecha_nacimiento": self.fecha_nacimiento,
            "direccion": self.direccion,
            "telefono": self.telefono,
            "correo_electronico": self.correo_electronico,
            "genero": self.genero,
            "estado_civil": self.estado_civil,
            "ocupacion": self.ocupacion,
            "informacion_adicional": self.informacion_adicional
        }

    def __str__(self):
        return f'Nombre: {self.nombre_apellido}\nRUT: {self.rut}\nFecha de nacimiento: {self.fecha_nacimiento}\nDirección: {self.direccion}\nTeléfono: {self.telefono}\nCorreo electrónico: {self.correo_electronico}\nGénero: {self.genero}\nEstado civil: {self.estado_civil}\nOcupación: {self.ocupacion}\nInformación adicional: {self.informacion_adicional}'
    
    