'''
小东和三个朋友一起在楼上抛小球，他们站在楼房的不同层，假设小东站的楼层距离地面N米，球从他手里自由落下，每次落地后反跳回上次下落高度的一半，并以此类推知道全部落到地面不跳，求4个小球一共经过了多少米？(数字都为整数)给定四个整数A,B,C,D，请返回所求结果。
  测试样例：
  100,90,80,70
  返回：1020
思路：解法一：这四个小球到最后不动的规律其实是一样的，因此可以加在一起算一个整个的高度落下，都是先经过一个下落高度x，然后走两倍的x/2，因为有弹起和回落，然后走两倍的x/4。一直减小到0.因此可以用while循环做。解法二：使用极限求解，实际上最后是3倍的x。
'''
class Balls1:
    def calcDistanc(self,a,b,c,d):
        return 3*(a+b+c+d)


class Balls2:
    def calcDistanc(self, a, b, c, d):
        x=a+b+c+d #x表示四个球离地面距离之和
        sum=x
        x = x/2.0
        while x>0:
            sum += 2*x
            x=x/2.0
        return int(sum)


if __name__=="__main__":
    print(Balls1().calcDistanc(100, 90, 80, 70))
    print(Balls2().calcDistanc(100, 90, 80, 70))
