lessoncount = int(input("Kaç adet ders notu gireceksiniz"))

passedExams = 0
failedExams = 0

for i in range(lessoncount):
   lessonExam1 = float(input(f"{i+1}. ders için vize notunu giriniz"))
   lessonExam2 = float(input(f"{i+1}. ders için final notunu giriniz"))
   totalExamNote = (lessonExam1 * 0.4) + (lessonExam2 * 0.6)
   if totalExamNote >= 50:
    passedExams += 1
else:
    failedExams += 1
i+=1

print(f"{passedExams} adet dersten geçtiniz. {failedExams} adet dersten kaldınız.")


     
    