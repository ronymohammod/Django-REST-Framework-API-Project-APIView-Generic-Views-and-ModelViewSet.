from django.db import models




class BlogModel(models.Model):
    TYPES ={
    }

    blog_title=models.TextField(max_length=100,null=True)
    content=models.CharField(max_length=100,null=True)
    author = models.CharField(max_length=100,null=True)
    category=models.CharField(max_length=100,null=True)

    def __str__(self):
        return f'{self.blog_title}'



class CourseModel(models.Model):

    course_title=models.TextField(max_length=100,null=True)
    description=models.TextField(max_length=100,null=True)
    course_fee = models.FloatField(null=True)
    admission_date=models.DateField(null=True)

    def __str__(self):
        return f'{self.course_title}'





class CourseCategoryModel(models.Model):

    category_name=models.CharField(max_length=100,null=True)
    description=models.TextField(max_length=100,null=True)



class SubjectModel(models.Model):

    cname=models.CharField(max_length=100,null=True)
    category=models.CharField()
    description=models.TextField(max_length=100,null=True)
    teacher_name = models.CharField(max_length=100,null=True)
    credit = models.PositiveBigIntegerField(null=True)


    # Student = models.ForeignKey(
    # on_delete=models.CASCADE,
    # related_name='teacher_name',
    # null=True
    # )
    
    