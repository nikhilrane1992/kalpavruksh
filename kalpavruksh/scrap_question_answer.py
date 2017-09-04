from kalpavruksh.models import *
from django.contrib.auth.models import User
from uuid import uuid4

questions_ans = [
	{
		"question": "What is cloud computing?",
		"answer":"Cloud computing allows the operation of application software with the help of internet - enabled devices. Clouds can be classified as public, private or hybrid."
	},
	{
		"question": "What is a B. Tech in Computer science in cloud computing course all about?",
		"answer": "The course includes computer operations on various languages, data generation and collection of information. The course imparts the basic as well as the latest knowledge concerning to the rapidly developing field of computers."
	},
	{
		"question": "Which college in India provide a B. Tech course in Computer Science in Cloud Computing?",
		"answer": "Apeejay Stya University, Gurgaon"
	},
	{
		"question": "What is the eligibility criteria?",
		"answer": "Candidates should have passed 10+2 with a minimum of 50% marks with Physics, Mathematics and Chemistry as major subjects."
	},
	{
		"question": "Is there a requirement of any entrance exams?",
		"answer": "The candidates should also have a valid score in UPSEE, JEE MAINS, BITSAT and the Apeejay Entrance Test."},
	{
		"question": "What is the admission procedure?",
		"answer": "Admissions are based on the merit obtained in JEE Mains, UPSEE, ASU test, BITSAT, followed by a counseling session."},
	{
		"question": "What is the duration of the program?",
		"answer": "The duration of the program is four years and it is spread over 8 semesters."
	},
	{
		"question": "What is the fee structure?",
		"answer": "The total fee structure for the course is around Rupees 9, 00, 000."
	},
	{
	"question": "What are the career prospects?",
	"answer": "The cloud computing industry is witnessing an explosive growth. Students with a B. Tech degree in Computer Science in Cloud Computing are hired by companies such as SIEMENS, HCL, NDTV 24*7, Deloitte, ONGC etc. The industry has opened up a lot of employment opportunities in roles such as Cloud consultant, cloud engineer, data center engineer etc."
	}
]

for i in questions_ans:
	user = User.objects.get(id=1)
	question = Question.objects.create(title=i['question'], user=user)
	Answer.objects.create(body=i['answer'], user=user, question=question)	
	print i
Tenant.objects.create(name="Nikhil Rane", api_key=str(uuid4()))