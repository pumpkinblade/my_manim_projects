from manimlib.imports import *

class Cover(Scene):
    def construct(self):
        tex = TexMobject("p(n)", "=", "\\cdots").scale(3)
        tex[0].set_color(RED)
        tex[2].set_color(BLUE)
        self.add(tex)

class Forewords(Scene):
    def construct(self):
        quote = TextMobject("伟大的自然之书以数学为语言", color=BLUE)
        author = TextMobject("-伽利略", color=RED)
        quote.shift(1.*UP)
        author.next_to(quote, DOWN+RIGHT, buff=MED_LARGE_BUFF)
        self.play(FadeIn(quote))
        self.wait(3)
        self.play(Write(author), run_time=2.5)
        self.wait(3)

class Contents(Scene):
    def construct(self):
        text_group = VGroup(
            TextMobject("什么是分拆数"),
            TextMobject("分拆数的生成函数"),
            TextMobject("互异分拆"),
            TextMobject("Ferrer图"),
            TextMobject("五边形数定理")
        )

        sections = []
        for i, sc in enumerate(text_group):
            number = TextMobject("\\texttt{%d.}"%(i+1), color=BLUE)
            number.next_to(sc, LEFT)
            sections.append(VGroup(number, sc))
        sections = VGroup(*sections)
        sections.arrange_submobjects(DOWN, aligned_edge=LEFT, buff=LARGE_BUFF)


        self.play(FadeIn(sections), run_time=2)
        self.wait(1)

        for i in range(len(sections)):
            self.play(
                ApplyMethod(sections[:i].set_opacity, .2),
                ApplyMethod(sections[i].set_opacity, 1.),
                ApplyMethod(sections[i+1:].set_opacity, .2),
                run_time=2
            )
            self.wait(2)

class WhatIsPartition(Scene):
    def construct(self):
        title = Title("什么是分拆数").set_color(BLUE)
        self.play(Write(title))
        self.wait()

        text_group = VGroup(
            TextMobject("把一个正整数", "$n$", "写成一些", "无序的", "正整数之和"),
            TextMobject("例如："),
            TexMobject("3=2+1=1+1+1"),
            TextMobject("像", "$3=1+1+1$", "这样的和式称为", "分拆"),
            TextMobject("所谓", "无序", "，就如认为", "$3=2+1$", "和", "$3=1+2$", "是一个分拆"),
            TextMobject("所有分拆的个数就称之为", "分拆数", "，记作", "$p(n)$"),
            TextMobject("在这个例子中，", "$p(3)=3$", "。", "特别地，定义", "$p(0)=1$")
        )
        text_group.arrange_submobjects(DOWN, aligned_edge=LEFT, buff=MED_SMALL_BUFF+0.05)
        text_group.move_to(ORIGIN)
        text_group.shift(0.4*DOWN)
        text_group[0][1].set_color(RED)
        text_group[0][3].set_color(BLUE)
        text_group[2].set_color(YELLOW)
        text_group[2].shift(3.5*RIGHT)
        text_group[3][1].set_color(YELLOW)
        text_group[3][3].set_color(BLUE)
        text_group[4][1].set_color(BLUE)
        text_group[4][3].set_color(YELLOW)
        text_group[4][5].set_color(YELLOW)
        text_group[5][1].set_color(BLUE)
        text_group[5][3].set_color(RED)
        text_group[6][1].set_color(RED)
        text_group[6][4].set_color(RED)

        self.play(Write(text_group[0]))
        self.play(Write(text_group[1:3]), run_time=1.5)
        self.wait(0.5)
        self.play(Write(text_group[3]))
        self.wait(1.0)
        self.play(Write(text_group[4]), run_time=1.5)
        self.wait(1.0)
        self.play(Write(text_group[5]), run_time=1.5)
        self.wait(1.0)
        self.play(Write(text_group[6][:3]))
        self.wait(0.5)
        self.play(Write(text_group[6][3:]))
        self.wait(3)
        self.play(FadeOut(text_group), FadeOut(title))

class GenFuncOfPartition(Scene):
    def construct(self):
        title = Title("分拆数的生成函数").set_color(BLUE)
        self.play(Write(title))


        text_group = VGroup(
            TextMobject("从另外一个角度来看分拆，先来看个例子"),
            TextMobject("对于", "$5=2+2+1$", " $=1 \\cdot 1 + 2\\cdot 2$"),
            TextMobject("既然分拆和顺序无关，那么可以认为这个分拆是由"),
            TextMobject("一", "个", "$1$", "，", "两", "个", "$2$", "，组成的")
        )
        text_group.arrange_submobjects(DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF)
        text_group[1][1].set_color(YELLOW)
        text_group[1][2].set_color(YELLOW)
        text_group[3][0].set_color(BLUE)
        text_group[3][2].set_color(RED)
        text_group[3][4].set_color(BLUE)
        text_group[3][6].set_color(RED)
        self.play(Write(text_group[0]))
        self.play(Write(text_group[1][:2]))
        self.wait(1)
        self.play(Write(text_group[2]))
        self.play(Write(text_group[3]))
        self.wait(0.5)
        self.play(Write(text_group[1][2]))
        self.wait(3)
        self.play(FadeOut(text_group))

        text_group2 = VGroup(
            TextMobject("于是，对于", "$n$", "的一个分拆，可以认为它是由"),
            TextMobject("$x_1$", "个", "$1$", "，", "$x_2$", "个", "$2$", "，", "$\\cdots$", "，组成的"),
            TextMobject("即，", "$1x_1+2x_2+\\cdots=n$", "的每一个解都对应了一个分拆"),
            TextMobject("可以推出，上述方程的解的个数就是"),
            TextMobject("$(1+x+x^2+\\cdots)(1+x^2+x^4+\\cdots)\\cdots$", "中", "$x^n$", "的系数"),
            TextMobject("这也是分拆数", "$p(n)$", "的值"),
        )
        text_group2.arrange_submobjects(DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF)
        text_group2.shift(0.5*DOWN)
        text_group2[0][1].set_color(RED)
        text_group2[1][0].set_color(BLUE)
        text_group2[1][2].set_color(RED)
        text_group2[1][4].set_color(BLUE)
        text_group2[1][6].set_color(RED)
        text_group2[1][8].set_color(BLUE)
        text_group2[2][1].set_color(BLUE)
        text_group2[4][0].set_color(YELLOW)
        text_group2[4][2].set_color(YELLOW)
        text_group2[5][1].set_color(RED)
        self.play(Write(text_group2[0]))
        self.play(Write(text_group2[1]))
        self.wait(1)
        self.play(Write(text_group2[2]))
        self.wait(1)
        self.play(Write(text_group2[3]))
        self.wait(1)
        self.play(Write(text_group2[4]))
        self.wait(0.5)
        self.play(Write(text_group2[5]))
        self.wait(3)
        self.play(FadeOut(text_group2))

        tex_group3 = VGroup(TexMobject("\\therefore", "\\sum_{n=0}^\\infty p(n)x^n"),
                            TexMobject("=", "(1+x+x^2+\\cdots)(1+x^2+x^4+\\cdots)\\cdots"),
                            TexMobject("=", "\\frac{1}{1-x} \\frac{1}{1-x^2} \\cdots", "=", "\\prod_{k=1}^\\infty \\frac{1}{1-x^k}"))
        tex_group3.arrange_submobjects(DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF)
        tex_group3[0][1].set_color(BLUE)
        tex_group3[1][1].set_color(BLUE)
        tex_group3[2][1].set_color(BLUE)
        tex_group3[2][3].set_color(BLUE)
        equals = TexMobject("=")

        self.play(Write(tex_group3[0]))
        self.play(Write(tex_group3[1]))
        self.wait(0.5)
        self.play(Write(tex_group3[2][:2]))
        self.wait(0.5)
        self.play(Write(tex_group3[2][2:]))
        self.wait(2)

        self.play(FadeOut(tex_group3[0][0]), FadeOut(tex_group3[1]), FadeOut(tex_group3[2][:-1]))
        self.play(ApplyMethod(tex_group3[0][1].next_to, equals, LEFT), ApplyMethod(tex_group3[2][-1].next_to, equals, RIGHT))
        self.play(FadeIn(equals))
        self.wait(2)


class DifferentPartition(Scene):
    def construct(self):
        title = Title("互异分拆").set_color(BLUE)
        self.play(Write(title))

        text_group1 = VGroup(
            TextMobject("有时人们会关注一类特殊的分拆，它的每一项都不同"),
            TextMobject("例如：", "$10=5+3+2$"),
            TextMobject("称这样的分拆为", "互异分拆"),
            TextMobject("所有互异分拆的个数则被称为", "互异分拆数")
        )
        text_group1[1][1].set_color(YELLOW)
        text_group1[2][1].set_color(BLUE)
        text_group1[3][1].set_color(BLUE)
        text_group1.arrange_submobjects(DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF)

        self.play(Write(text_group1[0]))
        self.play(Write(text_group1[1]))
        self.wait(0.5)
        self.play(Write(text_group1[2]))
        self.wait(0.5)
        self.play(Write(text_group1[3]))
        self.wait(2)
        self.play(FadeOut(text_group1))

        text_group2 = VGroup(
            TextMobject("同样地，一个互异分拆也可以看作由", "$x_1$", "个", "$1$", "，" ),
            TextMobject("$x_2$", "个", "$2$", "，", "$\\cdots$", "相加而来"),
            TextMobject("但是，同一个数字不能出现两次或以上，", "于是，"),
            TextMobject("$x_1$", "，", "$x_2$", "，", "$\\cdots$", "的取值范围被限制在了", "$\\{0, 1\\}$"),
            TextMobject("此时方程", "$1x_1 + 2x_2 + \\cdots = n$", "的解的个数为"),
            TextMobject("$(1+x)(1+x^2)\\cdots=\\prod_{k=1}^\\infty (1+x^k)$", "中", "$x^n$", "的系数")
        )
        text_group2.arrange_submobjects(DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF)
        text_group2.shift(0.5*DOWN)
        text_group2[0][1].set_color(BLUE)
        text_group2[0][3].set_color(RED)
        text_group2[1][0].set_color(BLUE)
        text_group2[1][2].set_color(RED)
        text_group2[1][4].set_color(BLUE)
        text_group2[3][0].set_color(BLUE)
        text_group2[3][2].set_color(BLUE)
        text_group2[3][4].set_color(BLUE)
        text_group2[3][6].set_color(GREEN)
        text_group2[4][1].set_color(BLUE)
        text_group2[5][0].set_color(YELLOW)
        text_group2[5][2].set_color(YELLOW)

        self.play(Write(text_group2[:2]))
        self.wait(1)
        self.play(Write(text_group2[2][:-1]))
        self.wait(0.5)
        self.play(Write(text_group2[2][-1]), run_time=0.3)
        self.play(Write(text_group2[3]))
        self.wait(1)
        self.play(Write(text_group2[4]))
        self.wait(0.5)
        self.play(FadeIn(text_group2[5]))
        self.wait(3)
        self.play(FadeOut(text_group2))

        text_group3 = VGroup(
            TextMobject("因此，互异分拆数的生成函数是", "$\\prod_{k=1}^\\infty (1+x^k)$"),
            TextMobject("而分拆数的生成函数", "$\\prod_{k=1}^\\infty \\frac{1}{1-x^k}=\\prod_{k=1}^\\infty (1-x^k)^{-1}$"),
            TextMobject("它们都和", "$\\prod_{k=1}^\\infty (1-x^k)$", "非常相似"),
            TextMobject("所以接下来有必要去研究这个函数的含义")
        )
        text_group3.arrange_submobjects(DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF+0.2)
        text_group3[0][1].set_color(YELLOW)
        text_group3[1][1].set_color(BLUE)
        text_group3[2][1].set_color(RED)

        self.play(Write(text_group3[0]))
        self.wait(0.5)
        self.play(Write(text_group3[1]))
        self.wait(1)
        self.play(Write(text_group3[2]))
        self.wait(0.5)
        self.play(Write(text_group3[3]))
        self.wait(2)
        self.play(FadeOut(text_group3))

        text_group4 = VGroup(
            TextMobject("设想一个互异分拆"),
            TextMobject("$n=n_1+n_2+\\cdots+n_s$"),
            TextMobject("$\\Rightarrow$", "$x^n=x^{n_1} x^{n_2} \\cdots x^{n_s}$"),
            TextMobject("$\\Rightarrow$", "$(-1)^sx^n=(-x^{n_1})(-x^{n_2})\\cdots(-x^{n_s})$"),
            TextMobject("这个分拆为", "$\\prod_{k=1}^\\infty (1-x^k)$", "中", "$x^n$", "系数贡献了", "$(-1)^s$"),
            TextMobject("如果", "$s$", "是奇数，称这个分拆为", "奇互异分拆"),
            TextMobject("易知，奇互异分拆对于", "$x^n$", "系数的贡献是", "$-1$"),
            TextMobject("类似地，", "偶互异分拆", "的贡献是", "$1$")
        )
        text_group4.arrange_submobjects(DOWN, aligned_edge=LEFT, buff=MED_SMALL_BUFF)
        # text_group4.move_to(LEFT)
        text_group4.shift(0.3*DOWN+0.3*LEFT)
        text_group4[1:4].shift(RIGHT)
        text_group4[1].set_color(BLUE)
        text_group4[2][1].set_color(YELLOW)
        text_group4[3][1].set_color(RED)
        text_group4[4][1].set_color(RED)
        text_group4[4][3].set_color(YELLOW)
        text_group4[4][5].set_color(BLUE)
        text_group4[5][1].set_color(GREEN)
        text_group4[5][3].set_color(BLUE)
        text_group4[6][1].set_color(YELLOW)
        text_group4[6][3].set_color(BLUE)
        text_group4[7][1].set_color(BLUE)
        text_group4[7][3].set_color(BLUE)

        self.play(Write(text_group4[0]))
        self.play(Write(text_group4[1]))
        self.wait(0.5)
        self.play(Write(text_group4[2]))
        self.wait(0.5)
        self.play(Write(text_group4[3]))
        self.wait(1.5)
        self.play(Write(text_group4[4]))
        self.wait(0.5)
        self.play(Write(text_group4[5]))
        self.play(Write(text_group4[6]))
        self.wait(0.5)
        self.play(Write(text_group4[7]))
        self.wait(2)
        self.play(FadeOut(text_group4))

        text_group5 = VGroup(
            TextMobject("于是，在", "$\\prod_{k=1}^\\infty (1-x^k)$", "中，", "$x^n$", "系数等于", "$n$", "的"),
            TextMobject("偶互异分拆数", "$p_e(n)$", " $-$", "奇互异分拆数", "$p_o(n)$"),
            TextMobject("为了进一步研究", "$p_e(n)$", "与", "$p_o(n)$", "之间的关系，"),
            TextMobject("需要引入", "Ferrer图", "这一数学工具")
        )
        text_group5.arrange_submobjects(DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF)
        text_group5[0][1].set_color(RED)
        text_group5[0][3].set_color(RED)
        text_group5[0][5].set_color(RED)
        text_group5[1][1].set_color(YELLOW)
        text_group5[1][4].set_color(YELLOW)
        text_group5[2][1].set_color(YELLOW)
        text_group5[2][3].set_color(YELLOW)
        text_group5[3][1].set_color(BLUE)

        self.play(Write(text_group5[0]))
        self.play(Write(text_group5[1]))
        self.wait(1)
        self.play(Write(text_group5[2]))
        self.play(Write(text_group5[3]))
        self.wait(2)
        self.play(FadeOut(text_group5), FadeOut(title))

class FerrerGraph(Scene):
    def construct(self):
        title = Title("Ferrer图").set_color(BLUE)
        self.play(Write(title))

        text1 = TextMobject("用一些点的阵列表示一个分拆，", "例如").next_to(title, DOWN, aligned_edge=LEFT)
        text2 = TextMobject("这样的点阵图被称为", "Ferrer图", "，", "很多的命题都可以通过")
        text3 = TextMobject("Ferrer图来证明，比如接下来的", "五边形数定理")
        text2[1].set_color(BLUE)
        text3[1].set_color(BLUE)
        text2.next_to(text1, DOWN, aligned_edge=LEFT)
        text2.shift(4.*DOWN)
        text3.next_to(text2, DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF)

        self.play(Write(text1))
        fg_group1 = self.fg_anim([4, 2, 1], 1.0*UP+0.5*LEFT, color=RED)
        fg_group2 = self.fg_anim([4, 4, 2, 1], -1.0*UP+0.5*LEFT, color=GREEN)
        self.play(Write(text2[:-1]))
        self.wait(0.5)
        self.play(Write(VGroup(text2[-1], text3)))
        self.wait(3)
        self.play(FadeOut(VGroup(title, fg_group1, fg_group2, text1, text2, text3)))


    def fg_anim(self, ns, anchor=ORIGIN, animation=True, color=BLUE):
        fg = VGroup()
        fla = ["{0}=".format(sum(ns))]
        for i, ni in enumerate(ns):
            if i > 0:
                fla.append("+")
            fla.append(str(ni))
            fg.add(VGroup(*[Dot(i/2*DOWN+j/2*RIGHT, color=color) for j in range(ni)]))
        fla = TexMobject(*fla, color=color)
        leadsto = TexMobject("\\leadsto").move_to(anchor)
        fla.next_to(leadsto, LEFT, buff=LARGE_BUFF)
        fg.next_to(leadsto, RIGHT, buff=LARGE_BUFF)
        fg_group = VGroup(fla, leadsto, fg)

        # animation
        if animation:
            self.play(Write(fla))
            self.play(FadeInFrom(leadsto, LEFT))
            for i, ni in enumerate(ns):
                self.play(TransformFromCopy(fla[2*i+1], fg[i]), run_time=1.1)

        return fg_group

class PantagonTheorem(Scene):
    def construct(self):
        title = Title("五边形数定理").set_color(BLUE)
        self.play(Write(title))
        
        fg = self.ferrgraph([9, 8, 7, 5, 3], buff=1/1.2).set_color(RED)
        fg.move_to(0.3*UP)
        subtitles = VGroup(
            TextMobject("观察互异分拆数的Ferrer图"),
            TextMobject("最底下一行称为", "底", "，其点的数目记为", "$b$"),
            TextMobject("从最上面一行的最后一点开始连$45^{\\circ}$线段"),
            TextMobject("连成的最长线段称为", "坡", "，其点的数目记为", "$s$"))
        tex_s = TexMobject("s", color=YELLOW)
        tex_b = TexMobject("b", color=YELLOW)
        subtitles[1][1].set_color(BLUE)
        subtitles[1][3].set_color(YELLOW)
        subtitles[3][1].set_color(BLUE)
        subtitles[3][3].set_color(YELLOW)
        brace_b = Brace(fg[-1], direction=DOWN, color=BLUE)
        tex_b.next_to(brace_b, DOWN)
        slope = Line(fg[0][-1].get_center(), fg[2][-1].get_center(), color=RED)
        brace_s = Brace(slope, direction=RIGHT+DOWN, color=BLUE)
        tex_s.next_to(brace_s, RIGHT+DOWN)
        tex_s.shift(0.7*UL)
        for subt in subtitles:
            subt.move_to(3.4*DOWN)
        
        self.play(Write(subtitles[0]), FadeIn(fg), run_time=1.5)
        self.play(FadeOut(subtitles[0]))
        self.play(Write(subtitles[1]), ShowCreation(brace_b), FadeInFromDown(tex_b))
        self.wait(2)
        self.play(FadeOut(subtitles[1]))
        self.play(ShowCreation(slope), Write(subtitles[2]))
        self.play(FadeOut(subtitles[2]))
        self.play(Write(subtitles[3]), ShowCreation(brace_s), FadeInFromDown(tex_s))
        self.wait(3)
        self.play(FadeOut(VGroup(subtitles[3], brace_s, tex_s, brace_b, tex_b, slope, fg)))


        subtitle = TextMobject("尝试寻找奇偶互异分拆之间的一一对应")
        subtitle.to_edge(DOWN)
        text_group11 = VGroup(
            TextMobject("假如Ferrer图中，", "$b \\le s$", "，把Ferrer图的"),
            TextMobject("底变成坡，", "这时，Ferrer图仍然表示一个"),
            TextMobject("互异分拆，但是奇偶性已经发生变化了")
        ).scale(0.8)
        text_group11[0][1].set_color(YELLOW)
        text_group11.arrange_submobjects(DOWN, aligned_edge=LEFT, buff=LARGE_BUFF)
        text_group11.move_to(2*RIGHT)

        fg1 = self.ferrgraph([5, 4, 2]).set_color(BLUE)
        fg1.move_to(4*LEFT+1*UP)
        fg1_s = TexMobject("s=2", color=YELLOW).scale(0.8)
        fg1_b = TexMobject("b=2", color=YELLOW).scale(0.8)
        fg1_s.next_to(fg1[0][0], LEFT)
        fg1_b.next_to(fg1[1][0], LEFT)
        self.play(Write(subtitle))
        self.play(FadeOut(subtitle))
        self.play(FadeIn(fg1))
        self.play(Write(text_group11[0][:2]), FadeIn(fg1_s), FadeIn(fg1_b))
        self.wait(0.5)
        self.play(Write(VGroup(text_group11[0][2], text_group11[1][0])))
        self.play(ApplyMethod(fg1[-1].set_color, YELLOW))
        self.play(ApplyMethod(fg1[-1][0].move_to, fg1[0][-1].get_center()+1/2*RIGHT))
        self.play(ApplyMethod(fg1[-1][1].move_to, fg1[1][-1].get_center()+1/2*RIGHT))
        self.play(Write(VGroup(text_group11[1][1], text_group11[2])))
        self.wait(3)
        self.play(FadeOut(text_group11))
        
        fg2 = self.ferrgraph([5, 4, 3]).set_color(RED)
        fg2.move_to(4*LEFT+1.5*DOWN)
        fg2_s = TexMobject("s=3", color=YELLOW).scale(0.8)
        fg2_b = TexMobject("b=3", color=YELLOW).scale(0.8)
        fg2_s.next_to(fg2[0][0], LEFT)
        fg2_b.next_to(fg2[1][0], LEFT)
        text_group12 = VGroup(
            TextMobject("有一种情况，这样的变换不能进行，", "即"),
            TextMobject("当", "$b=s$", "时，并且坡与底有相交时，", "此时"),
            TexMobject("n", "=", "b", "+", "(b+1)", "+", "\\cdots", "+", "(b+b-1)"),
            TexMobject("=", "\\frac{3b^2-b}{2}", "=", "w(b)"),
            TextMobject("其中", "$w(b)$", "就是五边形数", "$\\sum_{k=1}^b 3k-2$"),
            TextMobject("这种情况的分拆具有", "$b$", "个部分。", "它对"),
            TextMobject("$\\prod_{k=1}^\\infty (1-x^k)$", "中", "$x^n$", "系数贡献为", "$(-1)^b$")
        ).scale(0.8)
        text_group12.arrange_submobjects(DOWN, aligned_edge=LEFT, buff=MED_SMALL_BUFF+0.1)
        text_group12.move_to(2*RIGHT+0.5*DOWN)
        text_group12[1][1].set_color(YELLOW)
        text_group12[2][0].set_color(RED)
        text_group12[2][2].set_color(RED)
        text_group12[2][4].set_color(RED)
        text_group12[2][6].set_color(RED)
        text_group12[2][8].set_color(RED)
        text_group12[3][1].set_color(RED)
        text_group12[3][3].set_color(BLUE)
        text_group12[4][1].set_color(BLUE)
        text_group12[4][3].set_color(BLUE)
        text_group12[5][1].set_color(BLUE)
        text_group12[6][0].set_color(YELLOW)
        text_group12[6][2].set_color(YELLOW)
        text_group12[6][4].set_color(YELLOW)

        self.play(Write(text_group12[0][:-1]))
        self.play(FadeIn(fg2), FadeIn(fg2_s), FadeIn(fg2_b))
        self.wait(0.5)
        self.play(ApplyMethod(fg2[-1][0].move_to, fg2[0][-1].get_center()+RIGHT/2))
        self.play(ApplyMethod(fg2[-1][1].move_to, fg2[1][-1].get_center()+RIGHT/2))
        self.play(ApplyMethod(fg2[-1][2].move_to, fg2[2][-1].get_center()+RIGHT/2))
        error = TexMobject("(\\times)", color=RED)
        error.next_to(fg2, DOWN)
        self.play(FadeIn(error))
        self.wait(0.5)
        self.play(FadeOut(error))
        self.play(
            ApplyMethod(fg2[-1][0].move_to, fg2[1][0].get_center()+DOWN/2),
            ApplyMethod(fg2[-1][1].move_to, fg2[1][1].get_center()+DOWN/2),
            ApplyMethod(fg2[-1][2].move_to, fg2[1][2].get_center()+DOWN/2),
            run_time=2
        )
        self.play(Write(VGroup(text_group12[0][-1], text_group12[1][:-1])))
        self.wait(0.5)
        self.play(Write(VGroup(text_group12[1][-1], text_group12[2][:2], text_group12[2][3], text_group12[2][5:8])))
        self.play(
            TransformFromCopy(fg2[-1], text_group12[2][2]),
            TransformFromCopy(fg2[-2], text_group12[2][4]),
            TransformFromCopy(fg2[-3], text_group12[2][-1]),
            run_time=2
        )
        self.wait(0.5)
        self.play(Write(text_group12[3]))
        self.wait(1)
        self.play(Write(text_group12[4]))
        self.wait(1)
        self.play(Write(text_group12[5][:-1]))
        self.play(Write(VGroup(text_group12[5][-1], text_group12[6])))
        self.wait(3)

        self.play(FadeOut(text_group12), FadeOut(VGroup(fg1, fg1_s, fg1_b)), FadeOut(VGroup(fg2, fg2_s, fg2_b)))

        text_group21 = VGroup(
            TextMobject("当", "$b > s$", "时，把坡变成底，", "这时"),
            TextMobject("也有一种情况例外，", "当", "$b=s+1$"),
            TextMobject("并且底和坡有相交时，", "此时，"),
            TexMobject("n", "=", "b+(b+1)+\\cdots+(b+s-1)"),
            TexMobject("=", "(s+1)+(s+2)+\\cdots+(s+s)"),
            TexMobject("=", "\\frac{s^2+s}{2}", "=", "w(-s)"),
            TextMobject("此时有", "$s$", "行，贡献为", "$(-1)^s$")
        ).scale(0.8)
        text_group21.arrange_submobjects(DOWN, aligned_edge=LEFT, buff=MED_SMALL_BUFF+0.1)
        text_group21.move_to(2*RIGHT+0.5*DOWN)
        text_group21[0][1].set_color(YELLOW)
        text_group21[1][2].set_color(YELLOW)
        text_group21[3][0].set_color(RED)
        text_group21[3][2].set_color(RED)
        text_group21[4][1].set_color(RED)
        text_group21[5][1].set_color(RED)
        text_group21[5][3].set_color(BLUE)
        text_group21[6][1].set_color(YELLOW)
        text_group21[6][3].set_color(BLUE)

        fg3 = self.ferrgraph([6, 5, 3]).set_color(BLUE)
        fg3.move_to(4*LEFT+1*UP)
        fg3_s = TexMobject("s=2", color=YELLOW).scale(0.8).next_to(fg3[0][0], LEFT)
        fg3_b = TexMobject("b=3", color=YELLOW).scale(0.8).next_to(fg3[1][0], LEFT)
        self.play(FadeIn(fg3), FadeIn(fg3_s), FadeIn(fg3_b))
        self.play(
            ApplyMethod(fg3[0][-1].set_color, YELLOW), 
            ApplyMethod(fg3[1][-1].set_color, YELLOW),
            Write(text_group21[0][:-1])
        )
        self.play(ApplyMethod(fg3[0][-1].move_to, fg3[-1][0].get_center()+1/2*DOWN))
        self.play(ApplyMethod(fg3[1][-1].move_to, fg3[-1][1].get_center()+1/2*DOWN))
        self.wait(1)

        fg4 = self.ferrgraph([6, 5, 4]).set_color(RED)
        fg4.move_to(4*LEFT+1.5*DOWN)
        fg4_s = TexMobject("s=3", color=YELLOW).scale(0.8).next_to(fg4[0][0], LEFT)
        fg4_b = TexMobject("b=4", color=YELLOW).scale(0.8).next_to(fg4[1][0], LEFT)
        self.play(Write(VGroup(text_group21[0][-1], text_group21[1][0])))
        self.play(FadeIn(fg4), FadeIn(fg4_s), FadeIn(fg4_b))
        self.play(Write(VGroup(text_group21[1][1:], text_group21[2][0])))
        self.play(ApplyMethod(fg4[0][-1].move_to, fg4[-1][0].get_center()+1/2*DOWN))
        self.play(ApplyMethod(fg4[1][-1].move_to, fg4[-1][1].get_center()+1/2*DOWN))
        self.play(ApplyMethod(fg4[2][-1].move_to, fg4[-1][2].get_center()+1/2*DOWN))
        error.next_to(fg4, DOWN)
        self.play(FadeIn(error))
        self.play(FadeOut(error))
        self.play(
            ApplyMethod(fg4[0][-1].move_to, fg4[0][-2].get_center()+1/2*RIGHT),
            ApplyMethod(fg4[1][-1].move_to, fg4[1][-2].get_center()+1/2*RIGHT),
            ApplyMethod(fg4[2][-1].move_to, fg4[2][-2].get_center()+1/2*RIGHT),
            run_time=2
        )
        self.play(Write(VGroup(text_group21[2][-1], text_group21[3])))
        self.play(Write(text_group21[4]))
        self.play(Write(text_group21[5]))
        self.wait(1)
        self.play(Write(text_group21[6]))
        self.wait(3)
        self.play(FadeOut(text_group21), FadeOut(VGroup(fg4, fg4_s, fg4_b)), FadeOut(VGroup(fg3, fg3_s, fg3_b)))

        text_group3 = VGroup(
            TextMobject("综上所述，"),
            TextMobject("$(n \\neq w(m)) \\wedge (n \\neq w(-m))$"),
            TextMobject("$\\Rightarrow$ ",  "$n$", "的奇偶互异分拆之间有一个一一对应"),
            TextMobject("$\\Rightarrow$ ", "$\\prod_{k=1}^\\infty (1-x^k)$", "中", "$x^n$", "系数为", "$0$"),
            TextMobject("$(n = w(m)) \\vee (n = w(-m))$", "  $\\Rightarrow$ ", "$x^n$", "系数为", "$(-1)^m$"),
            TexMobject("\\therefore \\prod_{k=1}^\\infty (1-x^k) = 1 + \\sum_{m=1}^\\infty (-1)^m(x^{w(m)}+x^{w(-m)})")
        ).scale(0.9)
        text_group3.arrange_submobjects(DOWN, aligned_edge=LEFT, buff=MED_SMALL_BUFF+0.1)
        text_group3.shift(0.3*DOWN)
        text_group3[1].set_color(RED)        
        text_group3[2][1].set_color(RED)        
        text_group3[3][1].set_color(BLUE)
        text_group3[3][3].set_color(BLUE)
        text_group3[3][5].set_color(BLUE)
        text_group3[4][0].set_color(RED)
        text_group3[4][2].set_color(BLUE)
        text_group3[4][4].set_color(BLUE)
        text_group3[5].set_color(BLUE)
        
        self.play(Write(text_group3[0]))
        self.play(Write(text_group3[1]))
        self.wait(0.5)
        self.play(Write(text_group3[2]))
        self.wait(0.5)
        self.play(Write(text_group3[3]))
        self.wait(1)
        self.play(Write(text_group3[4]), run_time=2)
        self.wait(1)
        self.play(FadeIn(text_group3[5]))
        self.wait(4)
        self.play(FadeOut(text_group3))

        text_group4 = VGroup(
            TexMobject("1", "=", "\\left(\\prod_{k=1}^\\infty \\frac{1}{1-x^k}\\right)\\left(\\prod_{k=1}^\\infty (1-x^k)\\right)"),
            TexMobject("=", "\\left(\\sum_{n=0}^\\infty p(n)x^n\\right)\\left(1+\\sum_{m=1}^\\infty (-1)^m(x^{w(m)}+x^{w(-m)})\\right)"),
            TexMobject("=", "\\sum_{n=0}^\\infty p(n)x^n+\\sum_{n=0}^\\infty\\sum_{m=1}^\\infty (-1)^m(p(n-w(m))+p(n-w(-m)))x^n"),
            TexMobject("\\therefore", "p(n)+\\sum_{m=1}^\\infty (-1)^m(p(n-w(m))+p(n-w(-m)))=0", "\\ , \\ p(0)=1"),
            TexMobject("\\Rightarrow", "p(n)=p(n-1)+p(n-2)-p(n-5)-p(n-7)+\\cdots")
        ).scale(0.8)
        text_group4.arrange_submobjects(DOWN, aligned_edge=LEFT, buff=MED_SMALL_BUFF)
        text_group4.shift(0.4*DOWN)
        text_group4[0][0].set_color(BLUE)
        text_group4[0][2].set_color(BLUE)
        text_group4[1][1].set_color(BLUE)
        text_group4[2][1].set_color(BLUE)
        text_group4[3][1].set_color(RED)
        text_group4[3][2].set_color(RED)
        text_group4[4][1].set_color(RED)
        self.play(Write(text_group4[0]))
        self.wait(0.5)
        self.play(Write(text_group4[1]), run_time=2)
        self.wait(0.5)
        self.play(Write(text_group4[2]), run_time=2.5)
        self.wait(1.5)
        self.play(Write(text_group4[3]), run_time=2.5)
        self.wait(1)
        self.play(Write(text_group4[4]), run_time=2.5)
        self.wait(5)
        self.play(FadeOut(text_group4), FadeOut(title), run_time=2)


    def ferrgraph(self, ns, buff=1/2):
        fg = VGroup()
        for i, ni in enumerate(ns):
            fg.add(VGroup(*[Dot(i*buff*DOWN+j*buff*RIGHT) for j in range(ni)]))
        return fg

class Summary(Scene):
    def construct(self):
        title = Title("总结").set_color(BLUE)
        self.play(Write(title))

        text_group = VGroup(
            VGroup(TextMobject("\\texttt{1.}", "分拆数", "$p(n)$", "的生成函数"), TexMobject("\\sum_{n=0}^\\infty p(n)x^n = \\prod_{k=1}^\\infty \\frac{1}{1-x^k}")),
            VGroup(TextMobject("\\texttt{2.}", "五边形数定理"), TexMobject("\\prod_{k=1}^\\infty (1-x^k) = 1 + \\sum_{m=1}^\\infty (-1)^m(x^{w(m)}+x^{w(-m)})")),
            VGroup(TextMobject("\\texttt{3.}", "分拆数的递推公式"), TexMobject("p(n)=\\sum_{m=1}^\\infty (-1)^{m-1}(p(n-w(m))+p(n-w(-m)))")),
        ).scale(0.9)
        text_group[0].arrange_submobjects(RIGHT)
        text_group[1].arrange_submobjects(RIGHT)
        text_group[2].arrange_submobjects(DOWN, aligned_edge=LEFT)
        text_group.arrange_submobjects(DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF)
        text_group[2][1].shift(RIGHT)
        text_group.shift(0.4*DOWN)
        text_group[0][0][0].set_color(BLUE)
        text_group[0][0][2].set_color(RED)
        text_group[0][1].set_color(RED)
        text_group[1][0][0].set_color(BLUE)
        text_group[1][1].set_color(YELLOW)
        text_group[2][0][0].set_color(BLUE)
        text_group[2][1].set_color(BLUE)

        self.wait(0.5)
        self.play(Write(text_group[0][0]))
        self.play(FadeInFrom(text_group[0][1], RIGHT))
        self.wait(1)
        self.play(Write(text_group[1][0]))
        self.play(FadeIn(text_group[1][1]))
        self.wait(1)
        self.play(Write(text_group[2][0]))
        self.play(FadeInFromDown(text_group[2][1]))
        self.wait(5)

        self.play(FadeOut(text_group), FadeOut(title))

class Thanks(Scene):
    def construct(self):
        text = TextMobject("感谢观看!", color=BLUE)
        thanks = TexMobject("Thanks!", color=BLUE)
        text.shift(UP)
        thanks.next_to(text, DOWN)
        self.play(FadeIn(thanks), FadeIn(text))
        self.wait(3)
        self.play(FadeOut(text), FadeOut(thanks))
        self.wait(1)
        animation_engine = TextMobject("make with ", "manim")
        animation_engine[1].set_color(BLUE)
        # animation_engine.arrange_submobjects(DOWN, buff=LARGE_BUFF)
        bgm = TextMobject("bgm: ", "《Panacea》 - Disaterpeace - Hyper Light Drifter")
        bgm.arrange_submobjects(DOWN, buff=LARGE_BUFF)
        bgm[1].set_color(RED)
        animation_engine.shift(2*UP)
        bgm.shift(DOWN)
        self.play(FadeIn(animation_engine))
        self.play(FadeIn(bgm))
        self.wait(5)
        self.play(FadeOut(bgm), FadeOut(animation_engine))
        self.wait(1)