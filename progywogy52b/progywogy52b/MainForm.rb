require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"
def int(text)     return text.to_i end
def float(text)   return text.to_f end
def str(text)     return text.to_s end
def list(obj)     return obj.to_a  end
def len(arr)      return arr.length end
def input(msg="") print msg; return gets end
def print(*args)  Kernel.print(*args, "\n") end
def round(x, y)   return float((x * 10**y).round) / 10**y end
def range(*args)  if len(args) == 1 then 
    return  list((0...args[0]).step(1)); elsif len(args) == 2 then 
    return  list((args[0]...args[1]).step(1)); elsif len(args) == 3 then 
    return  list((args[0]...args[1]).step(args[2])) end; end
class MyRandom;   def randint(min, max) return rand(max-min) + min; end; 
    def random() return rand() end; 
    def shuffle(arr) return arr.shuffle end; 
    def choice(arr) return arr[randint(0, len(arr))] end; 
end; $random = MyRandom.new(); $math = Math
MessageBox = System::Windows::Forms::MessageBox
class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@textBox1 = System::Windows::Forms::TextBox.new()
		@textBox2 = System::Windows::Forms::TextBox.new()
		@textBox3 = System::Windows::Forms::TextBox.new()
		@textBox4 = System::Windows::Forms::TextBox.new()
		@button1 = System::Windows::Forms::Button.new()
		@label1 = System::Windows::Forms::Label.new()
		@label2 = System::Windows::Forms::Label.new()
		@button2 = System::Windows::Forms::Button.new()
		@label3 = System::Windows::Forms::Label.new()
		@label4 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		@textBox1.Location = System::Drawing::Point.new(203, 71)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(100, 20)
		@textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		@textBox2.Location = System::Drawing::Point.new(295, 98)
		@textBox2.Name = "textBox2"
		@textBox2.Size = System::Drawing::Size.new(100, 20)
		@textBox2.TabIndex = 1
		# 
		# textBox3
		# 
		@textBox3.Location = System::Drawing::Point.new(295, 37)
		@textBox3.Name = "textBox3"
		@textBox3.Size = System::Drawing::Size.new(100, 20)
		@textBox3.TabIndex = 2
		# 
		# textBox4
		# 
		@textBox4.Location = System::Drawing::Point.new(319, 63)
		@textBox4.Name = "textBox4"
		@textBox4.Size = System::Drawing::Size.new(100, 20)
		@textBox4.TabIndex = 3
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.Maroon
		@button1.ForeColor = System::Drawing::Color.White
		@button1.Location = System::Drawing::Point.new(251, 307)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(39, 35)
		@button1.TabIndex = 4
		@button1.Text = "clear"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.GhostWhite
		@label1.Location = System::Drawing::Point.new(50, 135)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(100, 23)
		@label1.TabIndex = 5
		# 
		# label2
		# 
		@label2.BackColor = System::Drawing::Color.GhostWhite
		@label2.Location = System::Drawing::Point.new(587, 9)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(100, 23)
		@label2.TabIndex = 6
		# 
		# button2
		# 
		@button2.Location = System::Drawing::Point.new(641, 357)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(75, 23)
		@button2.TabIndex = 7
		@button2.Text = "clear"
		@button2.UseVisualStyleBackColor = true
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# label3
		# 
		@label3.Location = System::Drawing::Point.new(50, 158)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(100, 23)
		@label3.TabIndex = 8
		@label3.Text = "sum"
		@label3.Click { |sender, e| self.Label3Click(sender, e) }
		# 
		# label4
		# 
		@label4.Location = System::Drawing::Point.new(587, 40)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(100, 23)
		@label4.TabIndex = 9
		@label4.Text = "averege"
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.Plum
		self.ClientSize = System::Drawing::Size.new(967, 461)
		self.Controls.Add(@label4)
		self.Controls.Add(@label3)
		self.Controls.Add(@button2)
		self.Controls.Add(@label2)
		self.Controls.Add(@label1)
		self.Controls.Add(@button1)
		self.Controls.Add(@textBox4)
		self.Controls.Add(@textBox3)
		self.Controls.Add(@textBox2)
		self.Controls.Add(@textBox1)
		self.Name = "MainForm"
		self.Text = "progywogy52b"
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	def Button1Click(sender, e)
		num1 = int(@textBox1.Text)
		mum2 = (@textBox2.Text)
		num3 = int(@textBox3.Text)
		num4 = int(@textBox4.Text)
		sum = num1 + num2 + num3 + num4
		averege = num1 + num2 + num3 + num4 / 4
		@label2.text = "sum: "
		@label1.text = "averege: "
	end

	def Button2Click(sender, e)
		@label1.Text = ""
		@label2.Text = ""
		@textBox1.Text = ""
		@textBox2.Text = ""
		@textBox3.Text = ""
		@textBox4.Text = ""
	end

	def Label3Click(sender, e)
		
	end



	

	
end

