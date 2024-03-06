from django.db import models

# Create your models here.
class test(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
   
    class Meta:
     abstract = True

    def __str__(self):
        return self.name


class permission(test):
    permissionToOptions = models.ManyToManyField('option', through='permissionOptionRole')
    permissionToRoles = models.ManyToManyField('Role', through='permissionOptionRole')

    class Meta:
        db_table = 'permissions'
        verbose_name = 'permissions'
        
    def __str__(self):
        return self.name
    
class option(test):
    optionToPermissions = models.ManyToManyField(permission, through='permissionOptionRole')
    optionToRoles = models.ManyToManyField('Role', through='permissionOptionRole')
    
    class Meta:
        db_table = 'options'
        verbose_name = 'option'
    
    def __str__(self):
         return self.name

    
class role(test):
    roleToOptions = models.ManyToManyField(option, through='permissionOptionRole' )
    roleTopermissions = models.ManyToManyField(permission, through= 'permissionOptionRole')

    class Meta:
        db_table = 'roles'
        verbose_name ='role'

    def __str__(self):
        return self.name
    
class permissionOptionRole(models.Model):
    permission = models.ForeignKey(permission, on_delete=models.CASCADE, to_field ='id')
    option = models.ForeignKey(option, on_delete=models.CASCADE, to_field ='id')
    role = models.ForeignKey(role,on_delete=models.CASCADE, to_field ='id')
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now_add=True,null=True)

    class Meta:
        db_table = 'permission_option_role'
        verbose_name = 'permissionOptionRole'

