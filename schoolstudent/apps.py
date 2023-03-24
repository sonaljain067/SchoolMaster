from django.apps import AppConfig

class SchoolStudentConfig(AppConfig):
    name = 'schoolstudent'

    def ready(self):
        import schoolstudent.signals
