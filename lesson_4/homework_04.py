adventures_of_tom_sawer = """ 
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

qwe = ('qwpoeiqwoipeiopqw .... iopeqowipeoipqwopiepqwo'
       'psaodiiopasiopdapi .... dapsiodspoiaoipdas'
       'asdasdopiasipodasiop .... dasiopdaiops')

def task_1():
    print("Task 1:")
    print(qwe)
    replace_end_of_the_sentence = qwe.replace("\n", " ").replace("...."," ")
    print(replace_end_of_the_sentence)


if __name__ == "__name__":
    task_1()
