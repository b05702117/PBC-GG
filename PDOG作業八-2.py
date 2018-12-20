
class Xy :

	def __init__( self, x, y ) :

		self.x = int( x ) # x座標

		self.y = int( y ) # y座標

	def magnitude( self ) :

		return ( self.x ** 2 + self.y ** 2 ) ** ( 1 / 2 ) # 大小

	def IsSmallerThan( self, p ) : # 比大小

		if self.magnitude() < Xy( p[0], p[1] ).magnitude() :

			return True

		elif self.magnitude() > Xy( p[0], p[1] ).magnitude() :

			return False

		elif self.magnitude() == Xy( p[0], p[1] ).magnitude() and  self.x < self.y :

			return True

		else : 

			return False

xylist = []

anslist = []

num = int( input() ) # 點的數量

xx = [ int(i) for i in input().split( ) ] # x座標

yy = [ int(i) for i in input().split( ) ] # y座標

for i in range( num ) :

	anslist.append( i + 1 )  # [ 1, 2, 3, 4 ] 排序

for i in range( num ) :

	xylist.append( [ xx[i],yy[i] ] ) # xy座標

for i in range( num - 1 ) : # 跟在自己前面的比

	for j in range( i + 1 ) :

		if Xy( xylist[ i + 1 ][0], xylist[ i + 1 ][1] ).IsSmallerThan( xylist[ j ] ) :

			anslist.insert( j, i + 2 )

			anslist.pop( i + 2 )

			xylist.insert( j, xylist[ i + 1 ] )

			xylist.pop( i + 2 )

			break

for i in range( len( anslist ) ) :

	if i != len( anslist ) - 1 :

		print( anslist[i], end = ' ' ) 

	else : # 避免多印空格

		print( anslist[i] )

# 123






		
