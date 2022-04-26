from manim import *
from manim.utils.paths import path_along_circles

class Introduction(Scene):
	def construct(self):
		with register_font("CMUSerif-Roman.ttf"):
			welC = Text("Welcome to", font_size=52, font="CMU Serif")
			escE = Text("Essence of Quadratic Functions", color=YELLOW, font_size=52, font="CMU Serif")
			welC_TF = Text("In this interactive playground,", font_size=52, font="CMU Serif")
			obj2 = MarkupText(
				f'We’ll learn to graph a <span fgcolor="{YELLOW}">quadratic function</span>.', color=WHITE,  font_size=52 , font="CMU Serif"
			)	
			
		pondering_pi_alt= ImageMobject("pondering.png").scale(0.3)
		pondering_pi= ImageMobject("pondering_2.png").scale(0.3)
		up_pi= ImageMobject("looking-up.png").scale(0.3)
		confused_pi= ImageMobject("confused.png").scale(0.3)


		done = VGroup(welC, escE).arrange(DOWN, buff=0.4)
		done_TF = VGroup(welC_TF, obj2).arrange(DOWN, buff=0.4).shift(1.8*UP)

		self.play(Write(done), run_time=3)
		
class Objective_2(Scene):
			
			def construct(self):
				with register_font("CMUSerif-Roman.ttf"):
					goalObj = Text("Goals:", font="CMU Serif", font_size=44).shift(3.2*UP).shift(5.85*LEFT).set_z_index(50)
					goalObj1 = Text("1) Lean Quadratic func.", font="CMU Serif" , font_size=44,color=BLUE_C).next_to(goalObj, RIGHT).shift(0.055*DOWN).set_z_index(50)
					goalObj2 = Text("2) Graphing them", font="CMU Serif", font_size=44,color=GOLD_C).next_to(goalObj1, RIGHT).set_z_index(50)
					
					#Question 1
					pi_question1_line1 = Text("Graphing Quadratic", font="CMU Serif", font_size=38)
					pi_question1_line2 = Text("functions!??", font="CMU Serif", font_size=38)
					pi_question1 = VGroup(pi_question1_line1, pi_question1_line2).arrange(DOWN, buff=0.2).shift(1.07*LEFT, 0.33*UP)
					pi_question1_line1_transformAndFocus = Text("Graphing Quadratic Functions", font="CMU Serif", font_size=52).shift(UP*3.2)
					
					#Focus 1
					focus1_subtitle = MarkupText(
						f'Consider <span fgcolor="{WHITE}">one of the following</span> equations:', color=WHITE,  font="CMU Serif", font_size=46
					).next_to(pi_question1_line1_transformAndFocus, DOWN*2.0)
					focus1_subtitle_color = MarkupText(
						f'Consider <span fgcolor="{BLUE_B}">one of the following</span> equations:', color=WHITE,  font="CMU Serif", font_size=46
					).next_to(pi_question1_line1_transformAndFocus, DOWN*2.0)
					
					focus1_subtitle_caption1 = Text("Being the Interactive Project this is, You get to choose the", font="CMU Serif", font_size=34)
					focus1_subtitle_caption2 = Text("equation - but we will keep the options limited for the sake", font="CMU Serif", font_size=34)
					focus1_subtitle_caption3 = Text("of building up initial understanding with simpler functions.", font="CMU Serif", font_size=34)
					focus1_subtitle_caption = VGroup(focus1_subtitle_caption1, focus1_subtitle_caption2, focus1_subtitle_caption3).arrange(DOWN, buff=0.2).next_to(focus1_subtitle, DOWN*4)
									
					brace = Brace(mobject=focus1_subtitle[8:25],direction=DOWN, buff=0.14)
			
				pi_student_asking_with_bubble = ImageMobject("pi_images/pi_student_asking.png").scale(0.63).set_z_index(-2)
				pi_teacher_talking = ImageMobject("pi_images/pi_teacher_talking.png").scale(0.63).set_z_index(-2)
				pi_teacher_pointing = ImageMobject("pi_images/pi_teacher_pointing.png").scale(0.63).set_z_index(-2)
				pi_student_asking_no_bubble = ImageMobject("pi_images/pi_student_asking_no_bubble.png").scale(0.63).set_z_index(-2)
				
				pi_teacher_pointing_bye = ImageMobject("pi_images/pi_teacher_pointing.png").scale(0.63).set_z_index(-1).shift(DOWN*14)
			
				# self.play(Write(goalObj), FadeIn(pi_student_asking_no_bubble))
				# self.wait(0.8)
				# self.play(Write(goalObj1))
				# self.wait(0.8)
				# self.play(Write(goalObj2))
				# self.wait(0.8)
				# self.play(Write(pi_question1), AnimationGroup(ReplacementTransform(pi_student_asking_no_bubble, pi_student_asking_with_bubble, run_time=0.4)))
				
				# self.play(FadeIn(goalObj, goalObj1, goalObj2, pi_question1, pi_student_asking_with_bubble))
				# self.wait(1.6)
				
				self.play(ReplacementTransform(pi_student_asking_no_bubble, pi_teacher_pointing), FadeOut(goalObj, goalObj1, goalObj2), ReplacementTransform(pi_question1, pi_question1_line1_transformAndFocus))
				
				self.play(ReplacementTransform(pi_student_asking_no_bubble, pi_teacher_pointing), FadeOut(goalObj, goalObj1, goalObj2), ReplacementTransform(pi_question1, pi_question1_line1_transformAndFocus))

				self.remove(pi_student_asking_with_bubble)
				self.wait(0.8)
				self.play(Write(focus1_subtitle))
				self.wait(0.8)
				self.play(GrowFromCenter(brace), ReplacementTransform(focus1_subtitle, focus1_subtitle_color))
				self.play(ReplacementTransform(pi_teacher_pointing, pi_teacher_pointing_bye), AnimationGroup(Write(focus1_subtitle_caption, run_time=4.2)), )

class Objective_3(Scene):
			
			def construct(self):
				with register_font("CMUSerif-Roman.ttf"):
					goalObj = Text("Goals:", font="CMU Serif", font_size=44).shift(3.2*UP).shift(5.85*LEFT).set_z_index(50)
					goalObj1 = Text("1) Lean Quadratic func.", font="CMU Serif" , font_size=44,color=BLUE_C).next_to(goalObj, RIGHT).shift(0.055*DOWN).set_z_index(50)
					goalObj2 = Text("2) Graphing them", font="CMU Serif", font_size=44,color=GOLD_C).next_to(goalObj1, RIGHT).set_z_index(50)
					
					#Question 1
					pi_question1_line1 = Text("Graphing Quadratic", font="CMU Serif", font_size=38)
					pi_question1_line2 = Text("functions!??", font="CMU Serif", font_size=38)
					pi_question1 = VGroup(pi_question1_line1, pi_question1_line2).arrange(DOWN, buff=0.2).shift(1.07*LEFT, 0.33*UP)
					pi_question1_line1_transformAndFocus = Text("Graphing Quadratic Functions", font="CMU Serif", font_size=52).shift(UP*3.2)
					
					#Focus 1
					focus1_subtitle = MarkupText(
						f'Consider <span fgcolor="{WHITE}">one of the following</span> equations:', color=WHITE,  font="CMU Serif", font_size=46
					).next_to(pi_question1_line1_transformAndFocus, DOWN*2.0)
					
					focus1_obj3 = MarkupText(
						f'<span fgcolor="{BLUE_B}">Choose</span> an equation', color=WHITE,  font="CMU Serif", font_size=46
					).next_to(pi_question1_line1_transformAndFocus, DOWN*2.0)
					
					focus1_subtitle_color = MarkupText(
						f'Consider <span fgcolor="{BLUE_B}">one of the following</span> equations:', color=WHITE,  font="CMU Serif", font_size=46
					).next_to(pi_question1_line1_transformAndFocus, DOWN*2.0)
					
					focus1_subtitle_caption1 = Text("Being the Interactive Project this is, You get to choose the", font="CMU Serif", font_size=34)
					focus1_subtitle_caption2 = Text("equation - but we will keep the options limited for the sake", font="CMU Serif", font_size=34)
					focus1_subtitle_caption3 = Text("of building up initial understanding with simpler functions.", font="CMU Serif", font_size=34)
					focus1_subtitle_caption = VGroup(focus1_subtitle_caption1, focus1_subtitle_caption2, focus1_subtitle_caption3).arrange(DOWN, buff=0.2).next_to(focus1_subtitle, DOWN*4)
									
					brace = Brace(mobject=focus1_subtitle[8:25],direction=DOWN, buff=0.14)
			
				pi_student_asking_with_bubble = ImageMobject("pi_images/pi_student_asking.png").scale(0.63).set_z_index(-2)
				pi_teacher_talking = ImageMobject("pi_images/pi_teacher_talking.png").scale(0.63).set_z_index(-2)
				pi_teacher_pointing = ImageMobject("pi_images/pi_teacher_pointing.png").scale(0.63).set_z_index(-2)
				pi_student_asking_no_bubble = ImageMobject("pi_images/pi_student_asking_no_bubble.png").scale(0.63).set_z_index(-2)
				
				pi_teacher_pointing_bye = ImageMobject("pi_images/pi_teacher_pointing.png").scale(0.63).set_z_index(-1).shift(DOWN*14)
			
				EquationTitle1 = MathTex(r"f(x) = x^2 + 2.4x - 1", font_size=52).set_z_index(6)
				EquationTitle2 = MathTex(r"f(x) = 6x^2 - 12x + 3", font_size=52).set_z_index(6)
				EquationGroup = VGroup(EquationTitle1, EquationTitle2).arrange(LEFT, buff=1.6).shift(0.45*UP)

				rect1 = RoundedRectangle(corner_radius=0.05, height=0.98, width=5.4, stroke_width=2.8, stroke_color=BLUE_B).set_fill(DARKER_GREY, opacity=0.5).shift(0.44*UP, 3.3*RIGHT)
				rect2 = RoundedRectangle(corner_radius=0.05, height=0.98, width=5.5, stroke_width=2.8, stroke_color=BLUE_B).set_fill(DARKER_GREY, opacity=0.5).shift(0.44*UP, 3.2*LEFT)

				# self.play(Write(goalObj), FadeIn(pi_student_asking_no_bubble))
				# self.wait(0.8)
				# self.play(Write(goalObj1))
				# self.wait(0.8)
				# self.play(Write(goalObj2))
				# self.wait(0.8)
				# self.play(Write(pi_question1), AnimationGroup(ReplacementTransform(pi_student_asking_no_bubble, pi_student_asking_with_bubble, run_time=0.4)))
				
				# self.play(FadeIn(goalObj, goalObj1, goalObj2, pi_question1, pi_student_asking_with_bubble))
				# self.wait(1.6)
				
				


				self.add(pi_question1_line1_transformAndFocus, focus1_subtitle_color, focus1_subtitle_caption, brace, pi_teacher_pointing_bye)
				self.play(FadeOut(focus1_subtitle_caption,shift=DOWN), ReplacementTransform(focus1_subtitle_color, focus1_subtitle_color), ShrinkToCenter(brace), ReplacementTransform(pi_teacher_pointing_bye, pi_teacher_pointing), ReplacementTransform(focus1_subtitle_color, focus1_obj3))
				self.wait(1)
				self.play(AnimationGroup(Write(EquationTitle1), Write(EquationTitle2), run_time=1.6), AnimationGroup(Write(rect1), Write(rect2), run_time=1.2))

class Objective_1(Scene):

	def construct(self):
		with register_font("CMUSerif-Roman.ttf"):
			goalObj = Text("Goals:", font="CMU Serif", font_size=44).shift(3.2*UP).shift(5.85*LEFT).set_z_index(50)
			goalObj1 = Text("1) Lean Quadratic func.", font="CMU Serif" , font_size=44,color=BLUE_C).next_to(goalObj, RIGHT).shift(0.055*DOWN).set_z_index(50)
			goalObj2 = Text("2) Graphing them", font="CMU Serif", font_size=44,color=GOLD_C).next_to(goalObj1, RIGHT).set_z_index(50)
			
			#Question 1
			pi_question1_line1 = Text("Graphing Quadratic", font="CMU Serif", font_size=38)
			pi_question1_line2 = Text("functions!??", font="CMU Serif", font_size=38)
			pi_question1 = VGroup(pi_question1_line1, pi_question1_line2).arrange(DOWN, buff=0.2).shift(1.07*LEFT, 0.33*UP)
			pi_question1_line1_transformAndFocus = Text("Graphing Quadratic Functions", font="CMU Serif", font_size=52).shift(UP*3.2)
			
			#Focus 1
			focus1_subtitle = MarkupText(
				f'Consider <span fgcolor="{WHITE}">one of the following</span> equations:', color=WHITE,  font="CMU Serif", font_size=46
			).next_to(pi_question1_line1_transformAndFocus, DOWN*2.0)
			
			focus1_subtitle_color = MarkupText(
				f'Consider <span fgcolor="{BLUE_B}">one of the following</span> equations:', color=WHITE,  font="CMU Serif", font_size=46
			).next_to(pi_question1_line1_transformAndFocus, DOWN*2.0)
			
			focus1_subtitle_caption1 = Text("Being the Interactive Project this is, You get to choose the", font="CMU Serif", font_size=34)
			focus1_subtitle_caption2 = Text("equation - but we will keep the options limited for the sake", font="CMU Serif", font_size=34)
			focus1_subtitle_caption3 = Text("of building up initial understanding with simpler functions.", font="CMU Serif", font_size=34)
			focus1_subtitle_caption = VGroup(focus1_subtitle_caption1, focus1_subtitle_caption2, focus1_subtitle_caption3).arrange(DOWN, buff=0.2).next_to(focus1_subtitle, DOWN*4)
							
			brace = Brace(mobject=focus1_subtitle[8:25],direction=DOWN, buff=0.14)
	
		pi_student_asking_with_bubble = ImageMobject("pi_images/pi_student_asking.png").scale(0.63).set_z_index(-2)
		pi_teacher_talking = ImageMobject("pi_images/pi_teacher_talking.png").scale(0.63).set_z_index(-2)
		pi_teacher_pointing = ImageMobject("pi_images/pi_teacher_pointing.png").scale(0.63).set_z_index(-2)
		pi_student_asking_no_bubble = ImageMobject("pi_images/pi_student_asking_no_bubble.png").scale(0.63).set_z_index(-2)
		pi_confused_center = ImageMobject("pi_images/pi_confused_center.png").scale(0.63).set_z_index(-2)
		pi_teacher_pointing_bye = ImageMobject("pi_images/pi_teacher_pointing.png").scale(0.63).set_z_index(-1).shift(DOWN*14)
	
		self.play(Write(goalObj), FadeIn(pi_student_asking_no_bubble))
		self.wait(0.8)
		self.play(Write(goalObj1))
		self.wait(0.8)
		self.play(Write(goalObj2))
		self.wait(1.3)
		self.play(Write(pi_question1), AnimationGroup(ReplacementTransform(pi_student_asking_no_bubble, pi_student_asking_with_bubble, run_time=0.4)))
	
class Lesson_1(Scene):
		
		def construct(self):
			with register_font("CMUSerif-Roman.ttf"):
				goalObj = Text("Goals:", font="CMU Serif", font_size=44).shift(3.2*UP).shift(5.85*LEFT).set_z_index(50)
				goalObj1 = Text("1) Lean Quadratic func.", font="CMU Serif" , font_size=44,color=BLUE_C).next_to(goalObj, RIGHT).shift(0.055*DOWN).set_z_index(50)
				goalObj2 = Text("2) Graphing them", font="CMU Serif", font_size=44,color=GOLD_C).next_to(goalObj1, RIGHT).set_z_index(50)
				goalObj = Text("Goals:", font="CMU Serif", font_size=44).shift(3.2*UP).shift(5.85*LEFT).set_z_index(50)

				text = VGroup(
					Text("Hmm... plotting seems simple!", font="CMU Serif", font_size=38),
					Text("But how do we figure out where", font="CMU Serif", font_size=38),	
					Text("to put those red dots??", font="CMU Serif", font_size=38),									
				).arrange(DOWN, aligned_edge=LEFT).shift(1.8*UP, 1.8*RIGHT)
				
				
				text_color = VGroup(
					Text("Hmm... plotting seems simple!", font="CMU Serif", font_size=38),
					MarkupText(f'But <span fgcolor="{BLUE_B}">how do we figure out where</span>', color=WHITE,  font="CMU Serif", font_size=38),	
					MarkupText(f'<span fgcolor="{BLUE_B}">to put those red dots</span>??', color=WHITE,  font="CMU Serif", font_size=38),			
				).arrange(DOWN, aligned_edge=LEFT).shift(1.8*UP, 1.8*RIGHT)
				

				#Question 1
				pi_question1_line1 = Text("Graphing Quadratic", font="CMU Serif", font_size=38)
				pi_question1_line2 = Text("functions!??", font="CMU Serif", font_size=38)
				pi_question1 = VGroup(pi_question1_line1, pi_question1_line2).arrange(DOWN, buff=0.2).shift(1.07*LEFT, 0.33*UP)
				pi_question1_line1_transformAndFocus = Text("Graphing Quadratic Functions", font="CMU Serif", font_size=52).shift(UP*3.2)
				
				#Focus 1
				focus1_subtitle = MarkupText(
					f'Consider <span fgcolor="{WHITE}">one of the following</span> equations:', color=WHITE,  font="CMU Serif", font_size=46
				).next_to(pi_question1_line1_transformAndFocus, DOWN*2.0)
				
				focus1_subtitle_color = MarkupText(
					f'Consider <span fgcolor="{BLUE_B}">one of the following</span> equations:', color=WHITE,  font="CMU Serif", font_size=46
				).next_to(pi_question1_line1_transformAndFocus, DOWN*2.0)
				
				focus1_subtitle_caption1 = Text("Being the Interactive Project this is, You get to choose the", font="CMU Serif", font_size=34)
				focus1_subtitle_caption2 = Text("equation - but we will keep the options limited for the sake", font="CMU Serif", font_size=34)
				focus1_subtitle_caption3 = Text("of building up initial understanding with simpler functions.", font="CMU Serif", font_size=34)
				focus1_subtitle_caption = VGroup(focus1_subtitle_caption1, focus1_subtitle_caption2, focus1_subtitle_caption3).arrange(DOWN, buff=0.2).next_to(focus1_subtitle, DOWN*4)
								
				brace = Brace(mobject=focus1_subtitle[8:25],direction=DOWN, buff=0.14)
		
			pi_student_asking_with_bubble = ImageMobject("pi_images/pi_student_asking.png").scale(0.63).set_z_index(-2)
			pi_teacher_talking = ImageMobject("pi_images/pi_teacher_talking.png").scale(0.63).set_z_index(-2)
			pi_teacher_pointing = ImageMobject("pi_images/pi_teacher_pointing.png").scale(0.63).set_z_index(-2)
			pi_student_asking_no_bubble = ImageMobject("pi_images/pi_student_asking_no_bubble.png").scale(0.63).set_z_index(-2)
			pi_confused_center = ImageMobject("pi_images/pi_confused_center.png").scale(0.63).set_z_index(-4).shift(0.3*LEFT)
			pi_confused_center_down = ImageMobject("pi_images/pi_confused_center_down.png").scale(0.63).set_z_index(-4).shift(0.3*LEFT)

			pi_teacher_pointing_bye = ImageMobject("pi_images/pi_teacher_pointing.png").scale(0.63).set_z_index(-1).shift(DOWN*14)
		
			self.play(FadeIn(pi_confused_center))
			self.play(Write(text), run_time=2.8)
			self.play(ReplacementTransform(text, text_color))
			self.play(ReplacementTransform(pi_confused_center, pi_confused_center_down))
			self.wait(0.6)
			video_rect_bg = Rectangle(height=4.49999, width=8, stroke_width=3).set_fill(BLACK, opacity=1.0).scale(0.6).shift(1.45*DOWN, 3.2*RIGHT)
			self.play(Write(video_rect_bg), run_time=1.3)
			
			self.wait(7)

class Lesson_2(Scene):
	def construct(self):
	
		with register_font("CMUSerif-Roman.ttf"):
			tBubble1_1 = Text("It’s actually a", font="CMU Serif", font_size=44).set_z_index(50)
			tBubble1_2 = Text("very subtle idea", font="CMU Serif", font_size=44).set_z_index(50)
			tBubble1 = VGroup(tBubble1_1, tBubble1_2).arrange(DOWN, buff=0.2).shift(1.38*UP, 1.535*RIGHT)

			example = Text("Let’s see how...", font="CMU Serif", font_size=64).set_z_index(50).shift(UP*2)
			
			fn1_1 = Text("for a function, ", font="CMU Serif", font_size=44).set_z_index(50)
			fn1_2 = MathTex(r"f(x) = 2x^2 - 8x + 3", font_size=53, color=BLUE).set_z_index(50)
			fn1 = VGroup(fn1_1, fn1_2).arrange(RIGHT).shift(2.6*UP)
			fn2_1 =  Text("let’s say one vertex is ", font="CMU Serif", font_size=44).set_z_index(50)
			
			fanicer1 =  Text("basically, a fancier term", font="CMU Serif", font_size=35).set_z_index(48)
			fanicer2 =  Text("for those red dots!", font="CMU Serif", font_size=35).set_z_index(48)
			fanicer = VGroup(fanicer1, fanicer2).arrange(DOWN, aligned_edge=LEFT).shift(1.2*RIGHT, 0.1*UP)
				
			brace = Brace(mobject=fn2_1[13:20],direction=DOWN, buff=0.14).set_z_index(48).shift(1.245*LEFT, 1.65*UP)
			
			fn2_2 = MathTex(r"(x, y)", font_size=53, color=RED_C).set_z_index(66)
			fn2 = VGroup(fn2_1, fn2_2).arrange(RIGHT).next_to(fn1, DOWN).set_z_index(66)

			step1 = Text("Step 1: Draw a table", font="CMU Serif", font_size=44).set_z_index(50).shift(0.48*UP,0.6*RIGHT)
			
			anywhere = Text("Now this point can lie anywhere on the graph...", font="CMU Serif", font_size=38).set_z_index(65).shift(2.5*DOWN)
				
			
		# pi imports
		pi_student_asking_with_bubble = ImageMobject("pi_images/pi_student_asking.png").scale(0.63).set_z_index(-2)
		pi_teacher_talking = ImageMobject("pi_images/pi_teacher_talking.png").scale(0.63).set_z_index(-2)
		pi_teacher_pointing = ImageMobject("pi_images/pi_teacher_pointing.png").scale(0.63).set_z_index(-2)
		pi_student_asking_no_bubble = ImageMobject("pi_images/pi_student_asking_no_bubble.png").scale(0.63).set_z_index(-2)
		pi_confused_center = ImageMobject("pi_images/pi_confused_center.png").scale(0.63).set_z_index(-2)
		pi_teacher_pointing_bye = ImageMobject("pi_images/pi_teacher_pointing.png").scale(0.63).set_z_index(-1).shift(DOWN*14)
		teacher_happy_bubble = ImageMobject("pi_images/teacher_happy_bubble.png").scale(0.63).set_z_index(-2)
		teacher_happy_no_bubble = ImageMobject("pi_images/teacher_happy_no_bubble.png").scale(0.63).set_z_index(-2)
		papa_pi_29 = ImageMobject("pi_images/papa_pi_29.png").scale(0.63).set_z_index(-2)
		
		#table 
		t2 = MathTable(
		[["+", 0, 5, 10],
		[0, 0, 5, 10],
		[2, 2, 7, 12],
		[4, 4, 9, 14]],
		include_outer_lines=True)
		
		## 2x^2 - 8x + 3
		EquationTitle = MathTex(r"f(x) = 2x^2 - 8x + 3", font_size=52).next_to(example, DOWN*1.2).set_z_index(6)
		EquationTitle_RIGHT = MathTex(r"f(x) = 2x^2 - 8x + 3", font_size=52).set_z_index(6).shift(UP*3.3, 4.3*RIGHT)

		fullBlack_bye = Rectangle(height=8, width=14, stroke_width=0).set_fill(BLACK, opacity=1.0).shift(14*RIGHT).set_z_index(50)
		fullBlack_aye = Rectangle(height=8, width=14, stroke_width=0).set_fill(BLACK, opacity=1.0).set_z_index(55)

		self.play(FadeIn(teacher_happy_bubble), AnimationGroup(Wait(0.9), Write(tBubble1), lag_ratio=0.5, run_time=3))
		self.wait(1.8)
		self.play(ReplacementTransform(teacher_happy_bubble, pi_teacher_pointing), AnimationGroup(Wait(0.2), ReplacementTransform(tBubble1, example), lag_ratio=0.5))
		self.wait(1.8)
		self.play(ReplacementTransform(pi_teacher_pointing, pi_teacher_pointing_bye), FadeOut(example))
		

		# equation.add_background_rectangle(BLACK, 1)

		## COLOR
		# 
		
		ax = Axes().add_coordinates()
		dot_scene1 = Dot((2,1,0), color=RED).set_z_index(66)
		dot_scene2 = Dot((-4,2,0), color=RED).set_z_index(66)
		dot_scene3 = Dot((1,-3,0), color=RED).set_z_index(66)


		equation = MathTex(r"(x, y)", font_size=72).set_z_index(66)
		eq_bg_title = Rectangle(height=0.8, width=1.8, stroke_width=0).set_fill(BLACK, opacity=1.0).set_z_index(65)

		equation2 = MathTex(r"(x, y)", font_size=64).set_z_index(66).next_to(dot_scene1, RIGHT)
		eq_bg_title2 = Rectangle(height=0.8, width=1.8, stroke_width=0).set_fill(BLACK, opacity=1.0).set_z_index(65).next_to(dot_scene1, RIGHT).shift(0.28*LEFT)
		
		equation3 = MathTex(r"(x, y)", font_size=64).set_z_index(66).next_to(dot_scene2, RIGHT)
		eq_bg_title3 = Rectangle(height=0.8, width=1.8, stroke_width=0).set_fill(BLACK, opacity=1.0).set_z_index(65).next_to(dot_scene2, RIGHT).shift(0.28*LEFT)
		
		equation4 = MathTex(r"(x, y)", font_size=72).set_z_index(66)
		eq_bg_title4 = Rectangle(height=0.8, width=1.8, stroke_width=0).set_fill(BLACK, opacity=1.0).set_z_index(65)
		# equation4[0][1:2].set_color(RED_C)
		# equation4[0][3:4].set_color(YELLOW_C)
		
		equation5 = MathTex(r"(x, y)", font_size=78).set_z_index(66).shift(1.4*UP)
		eq_bg_title5 = Rectangle(height=0.8, width=1.8, stroke_width=0).set_fill(BLACK, opacity=1.0).set_z_index(65).shift(1.4*UP)
		equation5[0][1:2].set_color(RED_C)
		equation5[0][3:4].set_color(YELLOW_C)
		
		
		can_lie_anywhere = Rectangle(height=0.6, width=10.5, stroke_width=0).set_z_index(64).shift(2.5*DOWN).set_fill(BLACK, opacity=1.0)
		
		
		plane = NumberPlane(
		x_range=[-8,+8,1],
		y_range=[-5,5,1],	
		x_axis_config={"include_numbers": True, "label_direction": DL, "font_size":34,},
		
		y_axis_config={"include_numbers": True, "label_direction": DL, "font_size":34,},
		background_line_style={
			"stroke_width": 3,
		}).set_z_index(57)

		plane2 = NumberPlane(
		x_range=[-8,+8,1],
		y_range=[-5,5,1],	
		x_axis_config={"include_numbers": True, "label_direction": DL, "font_size":34,},
		
		y_axis_config={"include_numbers": True, "label_direction": DL, "font_size":34,},
		background_line_style={
			"stroke_width": 2,
		}).set_z_index(57).shift(14*RIGHT)
		
		# dot_scene1 = Dot((-3,0.8,0), color=RED)

		## side bonds
		rect = RoundedRectangle(corner_radius=0.01, height=8, width=0.17, stroke_width=0).shift(7.094*LEFT).set_fill(BLACK, opacity=1.0).set_z_index(80)
		rect2 = RoundedRectangle(corner_radius=0.01, height=8, width=0.17, stroke_width=0, z_index=5).shift(7.094*RIGHT).set_fill(BLACK, opacity=1.0).set_z_index(80)
		

		arrowx = Arrow(start=RIGHT, end=LEFT).shift(DOWN).rotate(-1.94).set_z_index(72).arrange(RIGHT).shift(0.089*UP, 	1.125*LEFT).scale(0.8)
		arrowy = Arrow(start=RIGHT, end=LEFT).shift(DOWN).rotate(-1.14).set_z_index(72).arrange(RIGHT).shift(0.089*UP, 1.125*RIGHT).scale(0.8)
		findX = MathTex(r"-b/2a", font_size=68, color=RED_C).set_z_index(66).next_to(arrowx, DOWN, buff=0.4).shift(0.4*LEFT)
		findY = MathTex(r"f(-b/2a)", font_size=68, color=YELLOW_C).set_z_index(66).next_to(arrowy, DOWN, buff=0.4).shift(0.4*RIGHT)

		
		
		self.add(rect, rect2)
		# anywhere.add_background_rectangle(color=TEAL)

		self.play(Write(fn1), FadeIn(fullBlack_bye), run_time=2.6)
		self.play(Write(fn2), run_time=2.4)		
		self.wait(1.8)
		self.play(GrowFromCenter(brace))
		self.play(AnimationGroup(Write(fanicer), run_time=2.4))
		self.wait(1.8)
		self.play(ReplacementTransform(fullBlack_bye, fullBlack_aye),AnimationGroup(Wait(0.5),ReplacementTransform(fn2, equation), lag_ratio=0.5), AnimationGroup(Wait(0.5), Write(plane), lag_ratio=0.5, run_time=3.4), GrowFromCenter(eq_bg_title))
		self.wait(1)
		self.play(Write(anywhere), AnimationGroup(Wait(0.9),GrowFromEdge(can_lie_anywhere, LEFT), lag_ratio=0.5))
		self.wait(1.6)
		self.play(ReplacementTransform(equation, equation2), ReplacementTransform(eq_bg_title, eq_bg_title2))
		self.play(Write(dot_scene1))
		self.wait(0.8)
		self.play(FadeOut(dot_scene1), ReplacementTransform(equation2, equation3), ReplacementTransform(eq_bg_title2, eq_bg_title3))
		self.play(Write(dot_scene2))
		self.wait(0.8)
		self.play(FadeOut(dot_scene2), ReplacementTransform(equation3, equation4), ReplacementTransform(eq_bg_title3, eq_bg_title4))
		self.play(FadeOut(plane), FadeOut(anywhere))
		self.play(ReplacementTransform(equation4, equation5))
		self.play(Write(arrowx), Write(findX))
		self.wait()
		self.play(Write(arrowy), Write(findY))


class confo(Scene):
	def construct(self):
	
		with register_font("CMUSerif-Roman.ttf"):
			tBubble1_1 = Text("And... that's it!", font="CMU Serif", font_size=44).set_z_index(50)
			tBubble1_2 = Text("Have a splendid day.", font="CMU Serif", font_size=44).set_z_index(50)
			tBubble1 = VGroup(tBubble1_1, tBubble1_2).arrange(DOWN, buff=0.3).shift(2.44*UP)

			
		pi_student_asking_with_bubble = ImageMobject("pi_images/pi_student_asking.png").scale(0.63).set_z_index(-2)
		pi_teacher_talking = ImageMobject("pi_images/pi_teacher_talking.png").scale(0.63).set_z_index(-2)
		pi_teacher_pointing = ImageMobject("pi_images/pi_teacher_pointing.png").scale(0.63).set_z_index(-2)
		pi_student_asking_no_bubble = ImageMobject("pi_images/pi_student_asking_no_bubble.png").scale(0.63).set_z_index(-2)
		pi_confused_center = ImageMobject("pi_images/pi_confused_center.png").scale(0.63).set_z_index(-2)
		pi_teacher_pointing_bye = ImageMobject("pi_images/pi_teacher_pointing.png").scale(0.63).set_z_index(-1).shift(DOWN*14)
		teacher_happy_bubble = ImageMobject("pi_images/teacher_happy_bubble.png").scale(0.63).set_z_index(-2)
		teacher_happy_no_bubble = ImageMobject("pi_images/teacher_happy_no_bubble.png").scale(0.63).set_z_index(-2)
		papa_pi_29 = ImageMobject("pi_images/papa_pi_29.png").scale(0.63).set_z_index(-2)
		
		self.play(FadeIn(pi_teacher_talking),AnimationGroup(Wait(0.9), Write(tBubble1), lag_ratio=0.5, run_time=5))
		self.wait(0.4)
		


class Interactive(Scene):
		def construct(self):
			with register_font("CMUSerif-Roman.ttf"):
				intro_line_1 = Text("Now for the interactive part... for equation", font="CMU Serif", font_size=44)
				intro_line_2_mathtext = MathTex(r"(x, y)", font_size=64)
				intro_line_2_text = Text("Now for the interactive part... for equation", font="CMU Serif", font_size=44)
		
class Plotting(Scene):
	def construct(self):
		
		# this will show how a quadratic function looks like after all. mmmmmmmm
		plane = NumberPlane(
			x_range=[-8,+8,1],
			y_range=[-5,5,1],	
			x_axis_config={"include_numbers": True, "label_direction": DL, "font_size":34,},
			z_index=-1,
			y_axis_config={"include_numbers": True, "label_direction": DL, "font_size":34,},
			background_line_style={
				"stroke_width": 3,
			})
			
		rect = RoundedRectangle(corner_radius=0.01, height=8, width=0.17, stroke_width=0).shift(7.094*LEFT).set_fill(BLACK, opacity=1.0).set_z_index(50)
		
		rect2 = RoundedRectangle(corner_radius=0.01, height=8, width=0.17, stroke_width=0, z_index=5).shift(7.094*RIGHT).set_fill(BLACK, opacity=1.0)
		
		rect3 = RoundedRectangle(corner_radius=0.01, height=0.7, width=4.5, stroke_width=0).shift(3.55*UP).set_fill(BLACK, opacity=1.0).set_z_index(2)
		# self.add_foreground_mobjects(rect, rect2)

		def quadratic(x):
			return x**2.0+2.4*x-1.0 #Your function here
		function1 = plane.plot(quadratic, x_range=[-5, +5],).set_color(color=[YELLOW,BLUE])
		
		ax = Axes().add_coordinates()
		dot_scene1 = Dot((-3,0.8,0), color=RED)
		dot_scene2 = Dot((-2,-1.8,0), color=RED)
		dot_scene3 = Dot((-1.2,-2.44,0), color=RED)
		dot_scene4 = Dot((0,-1,0), color=RED)
		dot_scene5 = Dot((1,2.4,0), color=RED)
		
		self.add(rect, rect2, rect3)
		EquationTitle = MathTex(r"f(x) = x^2 + 2.4x - 1", font_size=48).shift(3.5*UP).set_z_index(6)
		EquationTitle_front = MathTex(r"f(x) = x^2 + 2.4x - 1", font_size=56).set_z_index(6)

		EquationTitle.add_background_rectangle(BLACK, 1)
		
		self.play(Write(EquationTitle_front), run_time=2, rate_func=rate_functions.ease_in_sine)
		self.wait(1.2)
		
		
		EquationTitle_front.add_background_rectangle(BLACK, 1)

		self.play(AnimationGroup(Write(plane,run_time=4), Transform(EquationTitle_front, EquationTitle)))
		self.wait(1.3)

		self.play(Write(dot_scene1), Write(dot_scene2),Write(dot_scene3), Write(dot_scene4), Write(dot_scene5), run_time=1.2)
		
		self.wait(1.8)
		self.play(Write(function1), run_time=1.4, rate_func=rate_functions.ease_in_sine)
		self.wait(1.4)

		rects_right = ax.get_riemann_rectangles(
			function1,
			dx=0.15,
			x_range=[-2.6, 0.4],
			show_signed_area=False,
			color=(BLUE, YELLOW),
		).shift(0.1*LEFT)
				
		arrow = Arrow(start=RIGHT, end=LEFT).next_to(rects_right).shift(DOWN).rotate(-0.4)

		self.play(Write(arrow), run_time=0.5)
		self.wait(0.8)
		self.play(Transform(arrow, target_mobject = Arrow(start=RIGHT, end=LEFT).next_to(rects_right).shift(RIGHT*0.2),
			  path_func = path_along_circles(0.25*PI, [-1,0,0])
			))
		self.wait(0.8)
		
		with register_font("CMUSerif-Roman.ttf"):
			nameEnd = Text("A Parabola", font_size=42, font="CMU Serif", z_index=4).next_to(arrow).shift(RIGHT*0.17)
		rect4 = RoundedRectangle(corner_radius=0.03, height=0.7, width=3.3, stroke_width=0).next_to(arrow).set_fill(BLACK, opacity=1.0).shift(RIGHT*0.05)
		
		self.play(Write(nameEnd), Write(rect4), run_time=1.2, rate_func=rate_functions.ease_in_sine)
		self.wait()


	
		class Plotting(Scene):
			def construct(self):
				
				# this will show how a quadratic function looks like after all. mmmmmmmm
				plane = NumberPlane(
					x_range=[-8,+8,1],
					y_range=[-5,5,1],	
					x_axis_config={"include_numbers": True, "label_direction": DL, "font_size":34,},
					z_index=-1,
					y_axis_config={"include_numbers": True, "label_direction": DL, "font_size":34,},
					background_line_style={
						"stroke_width": 3,
					})
					
				rect = RoundedRectangle(corner_radius=0.01, height=8, width=0.17, stroke_width=0).shift(7.094*LEFT).set_fill(BLACK, opacity=1.0).set_z_index(50)
				
				rect2 = RoundedRectangle(corner_radius=0.01, height=8, width=0.17, stroke_width=0, z_index=5).shift(7.094*RIGHT).set_fill(BLACK, opacity=1.0)
				
				rect3 = RoundedRectangle(corner_radius=0.01, height=0.7, width=4.5, stroke_width=0).shift(3.55*UP).set_fill(BLACK, opacity=1.0).set_z_index(2)
				# self.add_foreground_mobjects(rect, rect2)
		
				def quadratic(x):
					return x**2.0+2.4*x-1.0 #Your function here
				function1 = plane.plot(quadratic, x_range=[-5, +5],).set_color(color=[YELLOW,BLUE])
				
				ax = Axes().add_coordinates()
				dot_scene1 = Dot((-3,0.8,0), color=RED)
				dot_scene2 = Dot((-2,-1.8,0), color=RED)
				dot_scene3 = Dot((-1.2,-2.44,0), color=RED)
				dot_scene4 = Dot((0,-1,0), color=RED)
				dot_scene5 = Dot((1,2.4,0), color=RED)
				
				self.add(rect, rect2, rect3)
				EquationTitle = MathTex(r"f(x) = x^2 + 2.4x - 1", font_size=48).shift(3.5*UP).set_z_index(6)
				EquationTitle_front = MathTex(r"f(x) = x^2 + 2.4x - 1", font_size=56).set_z_index(6)
		
				EquationTitle.add_background_rectangle(BLACK, 1)
				
				self.play(Write(EquationTitle_front), run_time=2, rate_func=rate_functions.ease_in_sine)
				self.wait(1.2)
				
				
				EquationTitle_front.add_background_rectangle(BLACK, 1)
		
				self.play(AnimationGroup(Write(plane,run_time=4), Transform(EquationTitle_front, EquationTitle)))
				self.wait(1.3)
		
				self.play(Write(dot_scene1), Write(dot_scene2),Write(dot_scene3), Write(dot_scene4), Write(dot_scene5), run_time=1.2)
				
				self.wait(1.8)
				self.play(Write(function1), run_time=1.4, rate_func=rate_functions.ease_in_sine)
				self.wait(1.4)
		
				rects_right = ax.get_riemann_rectangles(
					function1,
					dx=0.15,
					x_range=[-2.6, 0.4],
					show_signed_area=False,
					color=(BLUE, YELLOW),
				).shift(0.1*LEFT)
						
				arrow = Arrow(start=RIGHT, end=LEFT).next_to(rects_right).shift(DOWN).rotate(-0.4)
		
				self.play(Write(arrow), run_time=0.5)
				self.wait(0.8)
				self.play(Transform(arrow, target_mobject = Arrow(start=RIGHT, end=LEFT).next_to(rects_right).shift(RIGHT*0.2),
					  path_func = path_along_circles(0.25*PI, [-1,0,0])
					))
				self.wait(0.8)
				
				with register_font("CMUSerif-Roman.ttf"):
					nameEnd = Text("A Parabola", font_size=42, font="CMU Serif", z_index=4).next_to(arrow).shift(RIGHT*0.17)
				rect4 = RoundedRectangle(corner_radius=0.03, height=0.7, width=3.3, stroke_width=0).next_to(arrow).set_fill(BLACK, opacity=1.0).shift(RIGHT*0.05)
				
				self.play(Write(nameEnd), Write(rect4), run_time=1.2, rate_func=rate_functions.ease_in_sine)
				self.wait()
	
	
class Plotting(Scene):
	def construct(self):
		
		# this will show how a quadratic function looks like after all. mmmmmmmm
		plane = NumberPlane(
			x_range=[-8,+8,1],
			y_range=[-5,5,1],	
			x_axis_config={"include_numbers": True, "label_direction": DL, "font_size":34,},
			z_index=-1,
			y_axis_config={"include_numbers": True, "label_direction": DL, "font_size":34,},
			background_line_style={
				"stroke_width": 3,
			})
			
		rect = RoundedRectangle(corner_radius=0.01, height=8, width=0.17, stroke_width=0).shift(7.094*LEFT).set_fill(BLACK, opacity=1.0).set_z_index(50)
		
		rect2 = RoundedRectangle(corner_radius=0.01, height=8, width=0.17, stroke_width=0, z_index=5).shift(7.094*RIGHT).set_fill(BLACK, opacity=1.0)
		
		rect3 = RoundedRectangle(corner_radius=0.01, height=0.7, width=4.5, stroke_width=0).shift(3.55*UP).set_fill(BLACK, opacity=1.0).set_z_index(2)
		# self.add_foreground_mobjects(rect, rect2)
	
		def quadratic(x):
			return x**2.0+2.4*x-1.0 #Your function here
		function1 = plane.plot(quadratic, x_range=[-5, +5],).set_color(color=[YELLOW,BLUE])
		
		ax = Axes().add_coordinates()
		dot_scene1 = Dot((-3,0.8,0), color=RED)
		dot_scene2 = Dot((-2,-1.8,0), color=RED)
		dot_scene3 = Dot((-1.2,-2.44,0), color=RED)
		dot_scene4 = Dot((0,-1,0), color=RED)
		dot_scene5 = Dot((1,2.4,0), color=RED)
		
		self.add(rect, rect2, rect3)
		EquationTitle = MathTex(r"f(x) = x^2 + 2.4x - 1", font_size=48).shift(3.5*UP).set_z_index(6)
		EquationTitle_front = MathTex(r"f(x) = x^2 + 2.4x - 1", font_size=56).set_z_index(6)
	
		EquationTitle.add_background_rectangle(BLACK, 1)
		
		self.play(Write(EquationTitle_front), run_time=2, rate_func=rate_functions.ease_in_sine)
		self.wait(1.2)
		
		
		EquationTitle_front.add_background_rectangle(BLACK, 1)
	
		self.play(AnimationGroup(Write(plane,run_time=4), Transform(EquationTitle_front, EquationTitle)))
		self.wait(1.3)
	
		self.play(Write(dot_scene1), Write(dot_scene2),Write(dot_scene3), Write(dot_scene4), Write(dot_scene5), run_time=1.2)
		
		self.wait(1.8)
		self.play(Write(function1), run_time=1.4, rate_func=rate_functions.ease_in_sine)
		self.wait(1.4)
	
		rects_right = ax.get_riemann_rectangles(
			function1,
			dx=0.15,
			x_range=[-2.6, 0.4],
			show_signed_area=False,
			color=(BLUE, YELLOW),
		).shift(0.1*LEFT)
				
		arrow = Arrow(start=RIGHT, end=LEFT).next_to(rects_right).shift(DOWN).rotate(-0.4)
	
		self.play(Write(arrow), run_time=0.5)
		self.wait(0.8)
		self.play(Transform(arrow, target_mobject = Arrow(start=RIGHT, end=LEFT).next_to(rects_right).shift(RIGHT*0.2),
		  	path_func = path_along_circles(0.25*PI, [-1,0,0])
			))
		self.wait(0.8)
		
		with register_font("CMUSerif-Roman.ttf"):
			nameEnd = Text("A Parabola", font_size=42, font="CMU Serif", z_index=4).next_to(arrow).shift(RIGHT*0.17)
		rect4 = RoundedRectangle(corner_radius=0.03, height=0.7, width=3.3, stroke_width=0).next_to(arrow).set_fill(BLACK, opacity=1.0).shift(RIGHT*0.05)
		
		self.play(Write(nameEnd), Write(rect4), run_time=1.2, rate_func=rate_functions.ease_in_sine)
		self.wait()



class Plotting2(Scene):
	def construct(self):
		
		# this will show how a quadratic function looks like after all. mmmmmmmm
		plane = NumberPlane(
			x_range=[-8,+8,1],
			y_range=[-5,5,1],	
			x_axis_config={"include_numbers": True, "label_direction": DL, "font_size":34,},
			z_index=-1,
			y_axis_config={"include_numbers": True, "label_direction": DL, "font_size":34,},
			background_line_style={
				"stroke_width": 3,
			})
			
		rect = RoundedRectangle(corner_radius=0.01, height=8, width=0.17, stroke_width=0).shift(7.094*LEFT).set_fill(BLACK, opacity=1.0).set_z_index(50)
		
		rect2 = RoundedRectangle(corner_radius=0.01, height=8, width=0.17, stroke_width=0, z_index=5).shift(7.094*RIGHT).set_fill(BLACK, opacity=1.0)
		
		rect3 = RoundedRectangle(corner_radius=0.01, height=0.7, width=4.5, stroke_width=0).shift(3.55*UP).set_fill(BLACK, opacity=1.0).set_z_index(2)
		# self.add_foreground_mobjects(rect, rect2)

		def quadratic(x):
			return 6*x**2.0-12*x+3 #Your function here
		function1 = plane.plot(quadratic, x_range=[-5, +5],).set_color(color=[YELLOW,BLUE])
				
		ax = Axes().add_coordinates()
		dot_scene1 = Dot((-1,21,0), color=RED)
		dot_scene2 = Dot((0,3,0), color=RED)
		dot_scene3 = Dot((1,-3,0), color=RED)
		dot_scene4 = Dot((2,3,0), color=RED)
		dot_scene5 = Dot((3,21,0), color=RED)
		
		self.add(rect, rect2, rect3)
		EquationTitle = MathTex(r"f(x) = 6x^2 - 12x + 3", font_size=48).shift(3.5*UP).set_z_index(6)
		EquationTitle_front = MathTex(r"f(x) = 6x^2 - 12x + 3", font_size=56).set_z_index(6)

		EquationTitle.add_background_rectangle(BLACK, 1)
		
		self.play(Write(EquationTitle_front), run_time=2, rate_func=rate_functions.ease_in_sine)
		self.wait(1.2)
		
		
		EquationTitle_front.add_background_rectangle(BLACK, 1)

		self.play(AnimationGroup(Write(plane,run_time=4), Transform(EquationTitle_front, EquationTitle)))
		self.wait(1.3)

		self.play(Write(dot_scene1), Write(dot_scene2),Write(dot_scene3), Write(dot_scene4), Write(dot_scene5), run_time=1.2)
		
		self.wait(1.8)
		self.play(Write(function1), run_time=1.4, rate_func=rate_functions.ease_in_sine)
		self.wait(1.4)

		rects_right = ax.get_riemann_rectangles(
			function1,
			dx=0.15,
			x_range=[-2.6, 0.4],
			show_signed_area=False,
			color=(BLUE, YELLOW),
		).shift(0.1*LEFT)
				
		arrow = Arrow(start=RIGHT, end=LEFT).next_to(dot_scene3).shift(2.6*RIGHT, 1.5*DOWN).rotate(-0.4).set_z_index(200)

		self.play(Write(arrow), run_time=0.5)
		self.wait(0.8)
		self.play(Transform(arrow, target_mobject = Arrow(start=RIGHT, end=LEFT).shift(2.6*RIGHT, 1.5*DOWN),
			  path_func = path_along_circles(0.25*PI, [-1,0,0])
			))
		self.wait(0.8)
		
		with register_font("CMUSerif-Roman.ttf"):
			nameEnd = Text("A Parabola", font_size=38, font="CMU Serif", z_index=4).next_to(arrow).shift(RIGHT*0.17).set_z_index(200)
		rect4 = RoundedRectangle(corner_radius=0.03, height=0.7, width=3, stroke_width=0).next_to(arrow).set_fill(BLACK, opacity=1.0).shift(RIGHT*0.04)
		
		self.play(Write(nameEnd), Write(rect4), run_time=1.2, rate_func=rate_functions.ease_in_sine)
		self.wait()
		
class PlottingForEmptyGraph(Scene):
	def construct(self):
		
		# this will show how a quadratic function looks like after all. mmmmmmmm
		plane = NumberPlane(
			x_range=[-8,+8,1],
			y_range=[-5,5,1],	
			x_axis_config={"include_numbers": True, "label_direction": DL, "font_size":34,},
			z_index=-1,
			y_axis_config={"include_numbers": True, "label_direction": DL, "font_size":34,},
			background_line_style={
				"stroke_width": 3,
			})
			
		rect = RoundedRectangle(corner_radius=0.01, height=8, width=0.17, stroke_width=0).shift(7.094*LEFT).set_fill(BLACK, opacity=1.0).set_z_index(50)
		
		rect2 = RoundedRectangle(corner_radius=0.01, height=8, width=0.17, stroke_width=0, z_index=5).shift(7.094*RIGHT).set_fill(BLACK, opacity=1.0)
		
		with register_font("CMUSerif-Roman.ttf"):
			nameEnd = Text("Tilt your device to use this feature", font_size=52, font="CMU Serif").set_z_index(54)
		rect4 = RoundedRectangle(corner_radius=0.03, height=0.7, width=11.3, stroke_width=0).set_z_index(52).set_fill(BLACK, opacity=1.0)
		
		self.add(plane, rect, rect2, rect4, nameEnd)
						
class PlottingForLesson1(Scene):
	def construct(self):
	
		# this will show how a quadratic function looks like after all. mmmmmmmm
		plane = NumberPlane(
			x_range=[-8,+8,1],
			y_range=[-5,5,1],	
			x_axis_config={"include_numbers": True, "label_direction": DL, "font_size":34,},
			z_index=-1,
			y_axis_config={"include_numbers": True, "label_direction": DL, "font_size":34,},
			background_line_style={
				"stroke_width": 3,
			})
			
		rect = RoundedRectangle(corner_radius=0.01, height=8, width=0.17, stroke_width=0).shift(7.094*LEFT).set_fill(BLACK, opacity=1.0).set_z_index(50)
		
		rect2 = RoundedRectangle(corner_radius=0.01, height=8, width=0.17, stroke_width=0, z_index=5).shift(7.094*RIGHT).set_fill(BLACK, opacity=1.0)
		
		rect3 = RoundedRectangle(corner_radius=0.01, height=0.7, width=4.5, stroke_width=0).shift(3.55*UP).set_fill(BLACK, opacity=1.0).set_z_index(2)
		# self.add_foreground_mobjects(rect, rect2)
		
		def quadratic(x):
			return x**2.0+2.4*x-1.0 #Your function here
		function1 = plane.plot(quadratic, x_range=[-5, +5],).set_color(color=[YELLOW,BLUE])
		
		ax = Axes().add_coordinates()
		dot_scene1 = Dot((-3,0.8,0), color=RED)
		dot_scene2 = Dot((-2,-1.8,0), color=RED)
		dot_scene3 = Dot((-1.2,-2.44,0), color=RED)
		dot_scene4 = Dot((0,-1,0), color=RED)
		dot_scene5 = Dot((1,2.4,0), color=RED)
		
		self.add(rect, rect2)
		EquationTitle = MathTex(r"f(x) = x^2 + 2.4x - 1", font_size=48).shift(3.5*UP).set_z_index(6)
		EquationTitle_front = MathTex(r"f(x) = x^2 + 2.4x - 1", font_size=56).set_z_index(6)
		
		EquationTitle.add_background_rectangle(BLACK, 1)
		
		# self.play(Write(EquationTitle_front), run_time=2, rate_func=rate_functions.ease_in_sine)
		# self.wait(1.2)
		# 
		
		# EquationTitle_front.add_background_rectangle(BLACK, 1)
		
		self.play(AnimationGroup(Write(plane,run_time=4)))
		self.wait(1.3)
		
		self.play(Write(dot_scene1), Write(dot_scene2),Write(dot_scene3), Write(dot_scene4), Write(dot_scene5), run_time=1.2)
		# 
		# self.wait(1.8)
		# self.play(Write(function1), run_time=1.4, rate_func=rate_functions.ease_in_sine)
		# self.wait(1.4)
		
		rects_right = ax.get_riemann_rectangles(
			function1,
			dx=0.15,
			x_range=[-2.6, 0.4],
			show_signed_area=False,
			color=(BLUE, YELLOW),
		).shift(0.1*LEFT)
				
		arrow = Arrow(start=RIGHT, end=LEFT, color=YELLOW).next_to(rects_right).shift(DOWN).rotate(-0.4)
		
		self.play(Write(arrow), run_time=0.5)
		self.wait(0.8)
		self.play(Transform(arrow, target_mobject = Arrow(start=RIGHT, end=LEFT).next_to(rects_right).shift(RIGHT*0.2),
	  		path_func = path_along_circles(0.25*PI, [-1,0,0])
			))
		self.wait(0.8)
		
		with register_font("CMUSerif-Roman.ttf"):
			nameEnd = Text("But, how??", font_size=42, font="CMU Serif", z_index=4).next_to(arrow).shift(RIGHT*0.25).shift(0.03*DOWN)
		rect4 = RoundedRectangle(corner_radius=0.03, height=0.7, width=3.3, stroke_width=0).next_to(arrow).set_fill(BLACK, opacity=1).shift(RIGHT*0.05)
		
		self.play(Write(nameEnd), Write(rect4), run_time=1.2, rate_func=rate_functions.ease_in_sine)
		self.wait()

class QuadraticFunctionEARLYFINAL(Scene):
		def construct(self):
			
			plane = NumberPlane(
				x_range=[-7,+7,1],
				y_range=[-4,4,1],
				x_axis_config={"include_numbers": True, "label_direction": DL, "font_size":34,"color": WHITE,},
				
				y_axis_config={"include_numbers": True, "label_direction": DL, "font_size":34, "color": WHITE,},
				background_line_style={
					"stroke_width": 3,
				})
				
			rect = RoundedRectangle(corner_radius=0.01, height=0.7, width=5.9, stroke_width=0).shift(3.5*UP).set_fill(BLACK, opacity=1.0)
			title = Text("Quadratic Function", font_size=48).shift(3.45*UP)
		
			def quadratic(x):
				return x**2+2*x-4 #Your function here
			function1 = plane.plot(quadratic, x_range=[-5,+5], color=YELLOW)
			self.play(Write(plane))
			self.add(rect)
			self.play(Write(title))
			self.play(Write(function1))
