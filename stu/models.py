from django.db import models

class Student(models.Model):
      학번 = models.IntegerField(primary_key=True) # 학번
      이름 = models.CharField(max_length =200) # 이름
      학년 = models.IntegerField(default=0) # 학년
      전화번호 = models.CharField(max_length =200) # 전화번호
      이메일 = models.CharField(max_length=200) # 이메일

      
      def __str__(self):
          return str(self.학번) + " " + self.이름
        

class Course(models.Model):
      과목번호 = models.IntegerField(primary_key=True) # 과목번호
      과목명 = models.CharField(max_length = 200) # 과목명
      학점 = models.IntegerField(default=0) # 학점
      is_전공 = models.BooleanField(default=True) # 전공과목여부

      def __str__(self):
          return str(self.과목번호) + " " +self.과목명


class Enrol(models.Model):
      학생 = models.ForeignKey(Student) # 외래키
      과목 = models.ForeignKey(Course) # 외래키
      성적 = models.DecimalField('성적',max_digits=10,decimal_places=2,default=0.00) # 성적
      수강학년 = models.IntegerField(default=0) # 수강학년
      수강학기 = models.IntegerField(default=0) # 수강 학기


      def __str__(self):
          return str(self.수강학년) +"학년 " +  str(self.수강학기) +"학기 성적 :" + str(self.성적)