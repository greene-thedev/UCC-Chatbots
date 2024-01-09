import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"


R_DEADLINE = "Our application deadline is typically in [month]. Please check our website for the exact date."


R_REQUIREMENT = "Admission requirements differ by program. You can find detailed information on our website or contact our admissions office."
R_SCHOLARSHIP = "We offer various scholarships based on academic merit and other criteria. Visit our scholarship page on the website for details."
R_TOUR = "We offer campus tours! To schedule a tour, visit our website or contact our admissions office for assistance."

R_APPLICATION = "The application process involves filling out an online application form on our website and submitting necessary documents."
R_DOCUMENT = "You may be required to submit the following documents as part of the application process:\n1. High school transcripts\n2. Standardized test scores (e.g., SAT, ACT)\n3. Letters of recommendation\n4. Personal statement or essay\n5. Resume or curriculum vitae\nPlease check the specific requirements for your desired program on our official website."

R_PROGRAM = "We offer a diverse range of programs including [list of programs]. You can explore our program offerings on the official website."

R_CONTACT = "You can contact our admissions office by phone at [phone number] or via email at [email address]. Our team is ready to assist you with any inquiries."
R_INTERFEES = "Tuition fees for international students vary by program. Please visit our website or contact the admissions office for detailed information on international tuition fees."
R_LIFE = "Campus life at our university is vibrant and diverse. Students engage in a variety of extracurricular activities, clubs, and events. You'll have the opportunity to make lifelong connections and create lasting memories."

R_HOUSING = "Our university provides various housing options for students, including on-campus dormitories and off-campus housing resources. For details on housing availability and application procedures, please visit our housing services page on the website."

R_ACTIVITIES = "We have a wide range of student activities and organizations catering to various interests. Whether you're interested in sports, arts, or community service, you'll find something that suits you. Explore our student activities on our website or visit the student center for more information."


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response