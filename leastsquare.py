from manimlib.imports import *

class Introduction(Scene):
    def construct(self):
        plane = NumberPlane()
        plane.add(plane.get_axis_labels())
        self.add(plane)

        self.intro()
        self.soln1()
        self.soln23()

    def y(self, x):
        return 1.4*x + 0.8

    def intro(self):
        X_value = np.array([-3., -2., -1.,  0.,  1.,  2.,  3.,])
        Y_value = np.array([
            -2.401521, -4.13425436, -1.47626429, -0.62544247,
            1.81823776, 2.83732628, 4.24002305
        ])
        XY_dots = VGroup(*list(map(Dot, np.c_[X_value, Y_value, np.zeros(shape=X_value.shape)])))
        XY_dots.set_color(BLUE)
        self.X_value = X_value
        self.Y_value = Y_value
        self.XY_dots = XY_dots

        self.line = FunctionGraph(self.y, x_min=-5, x_max=5, color=BLUE)
        self.line.rotate(-PI/12)
        self.line.shift(0.8*DOWN)

        text01 = TextMobject("问题的提出: ").scale(0.7)
        text02 = TextMobject("给定n个点,").scale(0.7)
        text03 = TexMobject("(x_1, y_1), \\dots, (x_n, y_n)", color=BLUE).scale(0.7)
        text04 = TextMobject("作出一条直线,").scale(0.7)
        text05 = TextMobject("尽可能地和这些点靠近").scale(0.7)
        text01.to_edge(UP+LEFT)
        text02.next_to(text01, DOWN, aligned_edge=LEFT)
        text03.next_to(text02, DOWN, aligned_edge=LEFT)
        text04.next_to(text03, DOWN, aligned_edge=LEFT)
        text05.next_to(text04, DOWN, aligned_edge=LEFT)
        
        self.play(Write(text01))
        self.play(
            FadeIn(XY_dots),
            Write(text02),
        )
        self.play(Write(text03))
        self.wait()
        self.play(
            ShowCreation(self.line),
            Write(text04),
            run_time=2
        )
        self.wait()
        self.play(
            ApplyMethod(self.line.rotate, PI/12),
            Write(text05)
        )
        self.wait()
        self.play(ApplyMethod(self.line.shift, 0.8*UP))
        self.wait()
        self.play(
            FadeOut(text01),
            FadeOut(text02),
            FadeOut(text03),
            FadeOut(text04),
            FadeOut(text05)
        )

    def soln1(self):
        self.td_Lines = []
        for x_, y_ in zip(self.X_value, self.Y_value):
            y1 = (0.8 + 1.4*x_ + 1.4*1.4*y_) / (1+1.4**2)
            x1 = (x_ + 1.4*y_ - 1.4*0.8) / (1+1.4**2)
            self.td_Lines.append(
                Line(x_*RIGHT+y_*UP, x1*RIGHT+y1*UP)
            )
        self.td_Lines_Group = VGroup(*self.td_Lines)
        self.td_Lines_Group.set_color(RED)

        text01 = TextMobject("方案一: ").scale(0.7)
        text02 = TextMobject("点到直线的距离的总和尽可能的小").scale(0.7)
        text03 = TextMobject("Minimize").scale(0.7)
        eq1 = TexMobject("\\sum_{i=1}^n \\frac{|Ax_i+By_i+C|}{\\sqrt{A^2+B^2}}", color=RED).scale(0.7)
        text01.to_edge(UP+LEFT)
        text02.next_to(text01, DOWN, aligned_edge=LEFT)
        text03.next_to(text02, DOWN, aligned_edge=LEFT, buff=1)
        eq1.next_to(text03, RIGHT)
        leq = TexMobject("Ax+By+C=0", color=BLUE)
        leq.to_edge(DR)

        self.play(Write(text01), FadeInFromDown(leq))
        self.play(
            Write(text02),
            ShowCreation(self.td_Lines_Group),
            run_time=2
        )
        self.wait(1)
        self.play(Write(text03))
        self.play(
            FadeOutAndShiftDown(self.td_Lines_Group),
            FadeInFromDown(eq1),
            run_time = 2
        )
        self.wait(1)
        self.play(
            FadeOut(text01),
            FadeOut(text02),
            FadeOut(text03),
            FadeOut(eq1),
            FadeOut(leq),
            run_time = 3
        )
        
    def soln23(self):
        self.d_Lines = []
        for x_, y_ in zip(self.X_value, self.Y_value):
            self.d_Lines.append(
                Line(x_*RIGHT+y_*UP, x_*RIGHT+self.y(x_)*UP)
            )
        self.d_Lines_Group = VGroup(*self.d_Lines)
        self.d_Lines_Group.set_color(YELLOW)

        leq = TexMobject("y=ax+b", color=BLUE)
        leq.to_edge(DR)
        text01 = TextMobject("方案二: ").scale(0.7)
        text02 = TextMobject("点到直线的Y轴距离的", "总和", "尽可能小").scale(0.7)
        minimize = TextMobject("Minimize").scale(0.7)
        eq01 = TexMobject("\\sum_{i=1}^n |ax_i+b-y_i|", color=YELLOW).scale(0.7)
        plus = TexMobject("+").scale(0.7)
        text01.to_edge(LEFT+UP)
        text02.next_to(text01, DOWN, aligned_edge=LEFT)
        minimize.next_to(text02, DOWN, aligned_edge=LEFT, buff=1)
        eq01.next_to(minimize, RIGHT)

        prevdline = self.d_Lines[0].copy()
        prevdline.next_to(minimize, RIGHT)
        plus_group = VGroup()
        dl_position = [prevdline.get_center()]
        for dline in self.d_Lines[1:]:
            p = plus.copy()
            p.next_to(prevdline, RIGHT)
            plus_group.add(p)

            dl = dline.copy()
            dl.next_to(p, RIGHT)
            dl_position.append(dl.get_center())
            prevdline = dl

        exp_group = VGroup(plus_group, self.d_Lines_Group)

        self.play(Write(text01), FadeInFromDown(leq))
        self.play(
            Write(text02),
            ShowCreation(self.d_Lines_Group),
            run_time = 3
        )
        self.play(Write(minimize))
        self.play(
            Write(plus_group),
            ApplyMethod(self.d_Lines[0].move_to, dl_position[0]),
            ApplyMethod(self.d_Lines[1].move_to, dl_position[1]),
            ApplyMethod(self.d_Lines[2].move_to, dl_position[2]),
            ApplyMethod(self.d_Lines[3].move_to, dl_position[3]),
            ApplyMethod(self.d_Lines[4].move_to, dl_position[4]),
            ApplyMethod(self.d_Lines[5].move_to, dl_position[5]),
            ApplyMethod(self.d_Lines[6].move_to, dl_position[6]),
            run_time = 2
        )
        self.wait(1)
        self.play(Transform(exp_group, eq01), run_time=2)
        self.wait(1)

        text03 = TextMobject("最小二乘法的方案: ").scale(0.7)
        text04 = TextMobject("平方和", color=RED).scale(0.7)
        text04.submobjects[0].set_color(RED)
        eq02 = TexMobject("\\sum_{i=1}^n (ax_i+b-y_i)^2", color=BLUE_C).scale(0.7)
        text03.move_to(text01.get_left(), aligned_edge=LEFT)
        eq02.move_to(eq01.get_left(), aligned_edge=LEFT)
        eq02_bg = SurroundingRectangle(VGroup(eq02, minimize), color=BLUE_E, fill_opacity=0.)
        eq02_group = VGroup(eq02, eq02_bg, minimize)

        self.play(
            FadeOutAndShiftDown(text01),
            FadeOutAndShiftDown(text02[1])
        )
        self.play(FadeInFromDown(text03))
        text04.next_to(text02.submobjects[0], RIGHT, buff=0.1)
        self.play(
            ApplyMethod(text02.submobjects[2].next_to, text04, RIGHT, {"buff":0.1}),
            FadeInFromDown(text04)
        )
        self.play(FadeOut(exp_group))
        self.play(FadeInFromDown(eq02))
        self.wait(2)
        self.clear()
        self.add(eq02, minimize)
        self.play(ShowCreation(eq02_bg))
        self.play(ApplyMethod(eq02_group.move_to, ORIGIN))
        self.wait(2)

class FormulaTransform(Scene):
    def construct(self):
        minimize = TextMobject("Minimize").scale(0.7)
        eq1 = TexMobject("\\sum_{i=1}^n (ax_i+b-y_i)^2", color=BLUE_C).scale(0.7)
        eq1.next_to(minimize, RIGHT)
        formula1_bg = SurroundingRectangle(VGroup(eq1, minimize), color=BLUE_E)
        formula1_group = VGroup(eq1, formula1_bg, minimize)
        formula1_group.move_to(ORIGIN)

        self.add(formula1_group)
        self.wait(1)
        self.play(FadeOut(formula1_bg), FadeOutAndShiftDown(minimize))
        self.play(ApplyMethod(eq1.shift, 3*LEFT))

        eq2_t = r'\begin{bmatrix} ax_1+b-y_1 \\ \vdots \\ ax_n+b-y_n \end{bmatrix}'
        text1 = TextMobject("将原来的式子改写成向量形式").scale(0.7)
        text1.to_edge(UL)
        vec1 = TexMobject(eq2_t, color=BLUE_C).scale(0.7)
        equals = TexMobject("=").scale(0.7)
        dot = TexMobject("\\dot").scale(0.7)
        equals.next_to(eq1, RIGHT)
        vec1.next_to(equals, RIGHT)
        dot.next_to(vec1, RIGHT)
        vec1_copy = vec1.copy()
        vec1_copy.next_to(dot, RIGHT)
        eq2_n1 = VGroup(vec1, dot, vec1_copy)
        self.play(
            Write(text1),
            Write(equals),
            Write(eq2_n1),
            run_time=2
        )
        eq2_n2 = TexMobject("\\left| %s \\right|^2"%eq2_t, color=BLUE_C).scale(0.7)
        eq2_n2.next_to(equals, RIGHT)
        eq2 = VGroup(eq2_n2, equals, eq1)
        self.play(FadeOut(eq2_n1))
        self.play(FadeInFromDown(eq2_n2))
        self.wait(1)
        self.play(ApplyMethod(eq2.next_to, text1, DOWN, {"aligned_edge":LEFT}))
        self.wait(1)

        text2 = TextMobject("考虑到直线的方程:").scale(0.7)
        lineq = TexMobject("y = ax+b = \\begin{bmatrix} x & 1 \\end{bmatrix} \\begin{bmatrix} a \\\\ b \\end{bmatrix}", color=RED).scale(0.7)
        text2.next_to(eq2, DOWN, aligned_edge=LEFT, buff=1)
        lineq.next_to(text2, RIGHT)
        self.play(Write(text2))
        self.play(Write(lineq), run_time=2)
        self.wait(1)

        text3 = TextMobject("设:").scale(0.7)
        text3.next_to(text2, DOWN, aligned_edge=LEFT)
        self.play(Write(text3))

        A = TexMobject("""
            A = \\begin{bmatrix}
                x_1 & 1 \\\\
                \\vdots & \\vdots \\\\
                x_n & 1
            \\end{bmatrix}
        """, color=BLUE_C).scale(0.7)
        A.next_to(text3, DOWN, aligned_edge=LEFT)
        A.shift(2.5*RIGHT)
        alpha = TexMobject("\\alpha = \\begin{bmatrix} a \\\\ b \\end{bmatrix}", color=BLUE_C).scale(0.7)
        alpha.next_to(A, RIGHT, buff=1)
        beta = TexMobject("\\beta = \\begin{bmatrix} y_1 \\\\ \\vdots \\\\ y_n \\end{bmatrix}", color=BLUE_C).scale(0.7)
        beta.next_to(alpha, RIGHT, buff=1)
        self.play(Write(A), Write(alpha), Write(beta))
        self.wait(2)

        eq3 = TexMobject("""
            = \\left| 
                \\begin{bmatrix}
                    ax_1 + b \\\\
                    \\vdots \\\\
                    ax_n + b \\\\
                \\end{bmatrix}
                - \\beta
            \\right|^2 = 
        """, color=BLUE_C).scale(0.7)
        eq4 = TexMobject("\\left| A\\alpha - \\beta \\right|^2", color=BLUE_C).scale(0.7)
        eq3.next_to(eq2, RIGHT)
        eq4.next_to(eq3, RIGHT)
        self.play(Write(eq3))
        self.wait(1)
        self.play(FadeInFrom(eq4, RIGHT))
        self.wait(1)

        propositions_bg = SurroundingRectangle(VGroup(A, alpha, beta), color=YELLOW)
        eq4_bg = SurroundingRectangle(eq4, color=YELLOW)
        self.play(ShowCreation(propositions_bg), ShowCreation(eq4_bg))
        self.wait(2)
        self.clear()
        self.wait(1)

        text1 = TextMobject("现在来重述问题").scale(0.7)
        text2 = TextMobject("给定一个m$\\times$n矩阵", "$A$", ", m>n, 以及一个n维向量", "$\\beta$").scale(0.7)
        text2.submobjects[1].set_color(BLUE_C)
        text2.submobjects[3].set_color(BLUE_C)
        text3 = TextMobject("求一个m维向量", "$\\alpha$", ", 使得").scale(0.7)
        text3.submobjects[1].set_color(BLUE_C)
        eq1 = TexMobject("\\left| A\\alpha - \\beta \\right| \\le \\left| A\\mathbf{X} - \\beta \\right|, \\forall \\mathbf{X} \\in \\mathbf{R}^m", color=BLUE_C).scale(0.7)
        text4 = TextMobject("其中向量", "$\\alpha$", "被称为线性方程组", "$A\\mathbf{X}=\\beta$", "的", "最小二乘解").scale(0.7)
        text4.submobjects[1].set_color(BLUE_C)
        text4.submobjects[3].set_color(BLUE_C)
        text4.submobjects[5].set_color(RED)
        text1.to_edge(UL)
        text1.shift(DOWN)
        text2.next_to(text1, DOWN, aligned_edge=LEFT)
        text3.next_to(text2, DOWN, aligned_edge=LEFT)
        eq1.next_to(text3, DOWN, aligned_edge=LEFT)
        text4.next_to(eq1, DOWN, aligned_edge=LEFT)
        eq1.shift(eq1.get_center()[0]*LEFT)
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
        self.wait(1)
        self.play(FadeIn(eq1))
        self.wait(1)
        self.play(Write(text4))
        self.wait(2)
        
class LinAlgProposition(Scene):
    def construct(self):
        self.abstract_definition()
        # self.proposition()
        # self.final_proof()
        # self.thanks()

    def abstract_definition(self):
        text1 = TextMobject("在探索最小二乘解的求法前, 先介绍一个重要的概念: ").scale(0.7)
        orth = TextMobject("正交投影", color=RED)
        text1.next_to(orth, UP)
        self.play(Write(text1))
        self.wait(1)
        self.play(FadeIn(orth))
        self.wait(1)
        self.play(FadeOut(text1), FadeOut(orth))
        text2 = TextMobject("正交投影的抽象定义: ").scale(0.7)
        text3 = TextMobject("设", "$U$", "是", "$\\mathbf{R}^n$", "的子空间, ", 
            "$\\alpha \\in \\mathbf{R}^n$", ", ", "$\\beta\\in U$", "称为", "$\\alpha$",
            "在", "$U$", "上的正交投影, 如果"
        ).scale(0.7)
        for i in [1, 3, 5, 7, 9, 11]:
            text3.submobjects[i].set_color(BLUE_C)
        eq1 = TexMobject("(\\alpha - \\beta) \\cdot \\gamma = 0, \\quad \\forall \\gamma \\in U", color=BLUE_C)
        text1.to_edge(UL)
        text2.next_to(text1, DOWN, aligned_edge=LEFT)
        text2.shift(DOWN)
        text3.next_to(text2, DOWN, aligned_edge=LEFT)
        eq1.next_to(text3, DOWN, aligned_edge=LEFT)
        eq1.shift(eq1.get_center()[0]*LEFT)
        self.play(Write(text2))
        self.play(Write(text3), run_time=2)
        self.wait(1)
        self.play(Write(eq1), run_time=2)
        self.wait(2)
        self.clear()

    def threeD_examplify(self):
        pass

    def proposition(self):
        text1 = TextMobject("一个重要的命题")
        self.play(FadeIn(text1))
        self.wait(1)
        self.play(FadeOut(text1))
        text2 = TextMobject("设", "$U$", "是", "$\\mathbf{R}^n$", 
            "的子空间, 对于", "$\\alpha \\in \\mathbf{R}^n$", ", 那么",  
            "$\\beta$", "是", "$\\alpha$", "在", "$U$", "的正交投影,"
        ).scale(0.7)
        word = TextMobject("当且仅当").scale(0.7)
        for i in [1, 3, 5, 7, 9, 11]:
            text2.submobjects[i].set_color(BLUE_C)
        eq1 = TexMobject("|\\alpha - \\beta| \\le |\\alpha - \\gamma|, \\quad \\forall \\gamma \\in U", color=BLUE_C)
        text2.shift(2*UP)
        word.next_to(text2, DOWN, aligned_edge=LEFT)
        self.play(Write(text2), run_time=2)
        self.play(Write(word))
        self.wait(1)
        self.play(FadeInFromDown(eq1))
        self.wait(2)
        self.clear()

    def final_proof(self):
        text1 = TextMobject("最终的证明")
        self.play(FadeIn(text1))
        self.wait(1)
        self.play(FadeOutAndShiftDown(text1))

        eq0 = TextMobject("$\\alpha$", "是线性方程组", "$A\\mathbf{X}=\\beta$", "的最小二乘解").scale(0.7)
        for i in [0, 2]:
            eq0.submobjects[i].set_color(BLUE_C)
        eq3 = TextMobject("$A\\alpha$", "是", "$\\beta$", "在", "$U$", "的正交投影").scale(0.7)
        for i in [0, 2, 4]:
            eq3.submobjects[i].set_color(BLUE_C)
        text1 = TextMobject("设", "$m \\times n$", "矩阵", "$A$", 
            "的列向量是", "$\\eta_1, \\dots, \\eta_n$", ", 设m维向量", "$\\beta$."
        ).scale(0.7)
        for i in [1, 3, 5, 7]:
            text1.submobjects[i].set_color(BLUE_C)
        text2 = TextMobject("设", "$U$", "是矩阵", "$A$", "的列空间, 即", "$U = \\left< \\eta_1, \\dots, \\eta_n \\right>$.").scale(0.7)
        for i in [1, 3, 5]:
            text2.submobjects[i].set_color(BLUE_C)
        eqtexts = [
            "$| A\\alpha - \\beta | \\le |A\\mathbf{v} - \\beta |, \\quad \\forall \\mathbf{v} \\in \\mathbf{R}^m$",
            "$| A\\alpha - \\beta | \\le |\\gamma - \\beta|, \\quad \\forall \\gamma \\in U$",
            "$\\gamma \\cdot (A\\alpha - \\beta) = 0, \\quad \\forall \\gamma \\in U$",
            "$\\gamma^T(A\\alpha - \\beta) = 0, \\quad \\forall \\gamma \\in U$",
            "$\\eta_i^T(A\\alpha - \\beta) = 0, \\quad i = 1, \\dots, n$",
            "$A^T(A\\alpha - \\beta) = 0$",
            "$A^TA\\alpha = A^T\\beta$"
        ]
        eqs = [TextMobject(t, color=BLUE_C).scale(0.7) for t in eqtexts]
        eqs = [eq0, *eqs[:2], eq3, *eqs[2:]]
        if_onlyif = [TexMobject("\\Leftrightarrow").scale(0.7) for i in range(1, len(eqs))]

        text1.to_edge(UL)
        text2.next_to(text1, DOWN, aligned_edge=LEFT)
        prevobj = eqs[0]
        prevobj.next_to(text2, DOWN, aligned_edge=LEFT)
        prevobj.shift(3*RIGHT)
        for i in range(1, len(eqs)):
            eqs[i].next_to(prevobj, DOWN, aligned_edge=LEFT)
            prevobj = eqs[i]
            if_onlyif[i-1].next_to(prevobj, LEFT)

        self.play(FadeInFromDown(text1))
        self.play(FadeInFromDown(text2))
        self.wait(2)
        self.play(Write(eqs[0]), run_time=2)
        for i in range(1, len(eqs)):
            self.play(FadeInFrom(if_onlyif[i-1], LEFT))
            if i == 3:
                self.play(Write(eqs[i]))
            else:
                self.play(FadeInFromDown(eqs[i]))
            self.wait(1)
        self.wait(3)

    def thanks(self):
        text = TextMobject("感谢观看!", color=BLUE)
        thanks = TexMobject("Thanks!", color=BLUE)
        text.shift(UP)
        thanks.next_to(text, DOWN)
        self.play(FadeIn(thanks), FadeIn(text))
        self.wait(3)
        self.play(FadeOut(text), FadeOut(thanks))
        self.wait(1)


class TwoDDemonstration(Scene):
    def construct(self):
        self.example1()
        self.example2()

    def example1(self):
        plane = NumberPlane()
        plane.add(plane.get_axis_labels())
        self.add(plane)

        U_line = Line(ORIGIN, 3*RIGHT-UP)
        U_sym = TexMobject("L")
        U_line.set_width(2*FRAME_WIDTH)
        U_sym.to_corner(DR)
        alpha_vec = Vector(3*RIGHT+2*UP, color=RED)
        alpha_sym = TexMobject("\\alpha", color=RED)
        alpha_sym.next_to(alpha_vec.get_end(), UL)
        subtitle1 = TextMobject("以二维平面为例")
        subtitle1.to_corner(DOWN)
        # self.play(ShowCreation(U_line), FadeInFromDown(U_sym), Write(subtitle1), run_time=3)
        # self.play(ShowCreation(alpha_vec), FadeInFromDown(alpha_sym), run_time=2)
        # self.wait(1)
        # self.play(FadeOut(subtitle1))

        # subtitle2 = TextMobject("过", "$\\alpha$", "的终点作垂线").scale(0.7)
        # subtitle2.to_corner(DOWN)
        beta_vec = Vector(7/10*(3*RIGHT-UP), color=GREEN_E)
        beta_sym = TexMobject("\\beta", color=GREEN_E)
        beta_sym.next_to(beta_vec, DOWN)
        delta_vec = Vector(alpha_vec.get_end() - beta_vec.get_end(), color=YELLOW)
        delta_vec.shift(beta_vec.get_end())
        D_line = Line(delta_vec.get_start(), delta_vec.get_end(), color=YELLOW).set_height(2*FRAME_HEIGHT)
        right_squre = Square(side_length=0.5, color=BLUE, fill_color=BLUE, fill_opacity=0.2)
        right_squre.next_to(ORIGIN, UL, buff=0)
        right_squre.rotate_about_origin(U_line.get_angle())
        right_squre.shift(beta_vec.get_end())
        # self.play(ShowCreation(D_line), run_time=2)
        # self.play(FadeIn(right_squre, DOWN))
        # self.wait(1)

        subtitle3 = TextMobject("$\\beta$就是$\\alpha$的正交投影")
        subtitle3.to_edge(DOWN)
        # self.play(ShowCreation(beta_vec), FadeInFromDown(beta_sym), run_time=2)
        # self.play(Write(subtitle3))
        # self.wait(2)
        # self.play(FadeOut(subtitle3))
        # self.wait(2)

        self.alpha_vec = alpha_vec
        self.alpha_sym = alpha_sym
        self.beta_vec = beta_vec
        self.beta_sym = beta_sym
        self.U_line = U_line
        self.U_sym = U_sym
        self.delta_vec = delta_vec
        self.numberplane = plane
        self.right_square = right_squre
        self.clear()

    def example2(self):
        self.add(self.numberplane)
        self.add(self.U_line, self.U_sym)
        self.add(self.alpha_vec, self.alpha_sym)
        self.add(self.beta_vec, self.beta_sym)
        alpha_vec = self.alpha_vec
        beta_vec = self.beta_vec
        delta_vec = self.delta_vec
        right_square = self.right_square
        delta_sym = TexMobject("\\alpha - \\beta", color=YELLOW).next_to(delta_vec, RIGHT)
        subtitile1 = TextMobject("仍以二维平面为例")
        subtitile1.to_edge(DOWN)
        self.play(FadeIn(subtitile1))
        self.play(ShowCreation(delta_vec), FadeInFromDown(delta_sym), run_time=2)
        self.play(FadeIn(right_square))
        self.wait(2)
        self.play(FadeOut(subtitile1))

        gamma_vec = Vector(-beta_vec.get_end(), color=PURPLE)
        gamma_sym = TexMobject("\\gamma", color=PURPLE)
        gamma_sym.next_to(gamma_vec, DOWN)
        delta_vec2 = Vector(alpha_vec.get_end() - gamma_vec.get_end(), color=BLUE)
        delta_sym2 = TexMobject("\\alpha - \\gamma", color=BLUE)
        delta_vec2.shift(gamma_vec.get_end())
        delta_sym2.next_to(delta_vec2, UP)
        delta_sym2.shift(0.5*LEFT)
        self.play(ShowCreation(gamma_vec), FadeInFromDown(gamma_sym), run_time=2)
        self.play(ShowCreation(delta_vec2), FadeInFromDown(delta_sym2), run_time=2)
        self.wait(2)

        for l in [-3, 3, -2]:
            gamma_vec2 = Vector(l*beta_vec.get_end(), color=gamma_vec.get_color())
            delta_vec3 = Vector(alpha_vec.get_end() - gamma_vec2.get_end(), color=delta_vec2.get_color())
            delta_vec3.shift(gamma_vec2.get_end())
            self.play(Transform(gamma_vec, gamma_vec2), Transform(delta_vec2, delta_vec3), run_time=3)
            self.wait(2)

        subtitle2 = TexMobject("|\\alpha - \\beta| \\le |\\alpha - \\gamma|", color=RED)
        subtitle2.to_edge(DOWN)
        self.play(FadeInFromDown(subtitle2))
        self.wait(3)
        subtitle3 = TextMobject("即: “点与直线之间垂线段最短”")
        subtitle3.to_edge(DOWN)
        self.play(FadeOut(subtitle2))
        # self.play(Write(subtitle3))
        self.wait(2)

class ThreeDDemonstration(SpecialThreeDScene):
    def construct(self):
        self.add(self.get_axes())
        self.set_camera_orientation(**self.get_default_camera_position())
        self.begin_ambient_camera_rotation(rate=0.005)
        plane = Square(side_length=20, color=None, fill_color=WHITE, fill_opacity=0.3)
        self.add(plane)

        alpha = Line(ORIGIN, 3*RIGHT-2*UP+2*OUT, color=RED)
        alpha_sym = TexMobject("\\alpha", color=RED).rotate(PI/2, RIGHT).next_to(alpha, OUT+RIGHT, buff=0.1)
        beta = Line(ORIGIN, 3*RIGHT-2*UP, color=GREEN)
        beta_sym = TexMobject("\\beta", color=GREEN).rotate(PI/2, RIGHT).next_to(beta, UP, buff=0.1)
        delta = Line(beta.get_end(), alpha.get_end(), color=YELLOW)
        delta_sym = TexMobject("\\alpha - \\beta", color=YELLOW).rotate(PI/2, RIGHT).next_to(delta, RIGHT, buff=0.1)
        gamma = Line(ORIGIN, -2*RIGHT-4*UP, color=PURPLE)
        gamma_sym = TexMobject("\\gamma", color=PURPLE).rotate(PI/2, RIGHT).next_to(gamma, UP, buff=0.1)
        xi = Line(gamma.get_end(), alpha.get_end(), color=BLUE)
        xi_sym = TexMobject("\\alpha - \\gamma", color=BLUE).rotate(PI/2, RIGHT).next_to(xi, DOWN, buff=0.1)
        eplison = Line(gamma.get_end(), beta.get_end(), color=PINK)
        right_square = Square(side_length=0.3, color=BLUE, fill_color=BLUE, fill_opacity=0.2)
        right_square.next_to(ORIGIN, UL, buff=0)
        right_square.rotate_about_origin(PI/2, RIGHT)
        right_square.rotate_about_origin(beta.get_angle(), OUT)
        right_square.shift(beta.get_end())
        self.wait()
        self.play(ShowCreation(alpha), FadeInFrom(alpha_sym, IN))
        self.wait()
        self.play(ShowCreation(delta))
        self.play(ShowCreation(beta), FadeInFrom(beta_sym, IN))
        self.play(FadeIn(right_square), FadeInFrom(delta_sym, IN))
        self.wait(1)

        another_right_square = right_square.copy()
        another_right_square.shift(-beta.get_end())
        rot_angle = beta.get_angle() - eplison.get_angle()
        another_right_square.rotate_about_origin(-rot_angle, OUT)
        another_right_square.shift(beta.get_end())
        self.play(ShowCreation(gamma), FadeInFrom(gamma_sym, IN))
        self.wait(1)
        self.play(ShowCreation(xi), FadeInFrom(xi_sym, IN))
        self.wait()
        self.play(ShowCreation(eplison))
        self.play(FadeIn(another_right_square))
        self.wait(2)

        self.play(FadeOut(another_right_square), FadeOut(xi_sym), FadeOut(gamma_sym))
        gamma_dir = [-5*RIGHT+1*UP, 3*RIGHT+4*UP, 4*RIGHT-4*UP, -2*RIGHT-4*UP]
        for gd in gamma_dir:
            gamma_t = Line(ORIGIN, gd, color=gamma.get_color())
            xi_t = Line(gamma_t.get_end(), alpha.get_end(), color=xi.get_color())
            eplison_t = Line(gamma_t.get_end(), beta.get_end(), color=eplison.get_color())

            self.play(
                Transform(gamma, gamma_t),
                Transform(xi, xi_t),
                Transform(eplison, eplison_t),
                run_time=2
            )
            self.wait(1)
        self.play(FadeIn(another_right_square), FadeIn(xi_sym), FadeIn(gamma_sym))
        self.wait(3)
        