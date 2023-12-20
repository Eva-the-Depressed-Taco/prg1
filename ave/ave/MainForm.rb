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
		@button3 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		@textBox1.Location = System::Drawing::Point.new(52, 44)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(100, 20)
		@textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		@textBox2.Location = System::Drawing::Point.new(52, 71)
		@textBox2.Name = "textBox2"
		@textBox2.Size = System::Drawing::Size.new(100, 20)
		@textBox2.TabIndex = 1
		# 
		# textBox3
		# 
		@textBox3.Location = System::Drawing::Point.new(52, 98)
		@textBox3.Name = "textBox3"
		@textBox3.Size = System::Drawing::Size.new(100, 20)
		@textBox3.TabIndex = 2
		# 
		# textBox4
		# 
		@textBox4.Location = System::Drawing::Point.new(52, 125)
		@textBox4.Name = "textBox4"
		@textBox4.Size = System::Drawing::Size.new(100, 20)
		@textBox4.TabIndex = 3
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.Plum
		@button1.Location = System::Drawing::Point.new(52, 152)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(75, 23)
		@button1.TabIndex = 4
		@button1.Text = "ave"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.Pink
		@label1.Location = System::Drawing::Point.new(52, 213)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(100, 23)
		@label1.TabIndex = 5
		# 
		# label2
		# 
		@label2.BackColor = System::Drawing::Color.Pink
		@label2.Location = System::Drawing::Point.new(52, 240)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(100, 23)
		@label2.TabIndex = 6
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.Plum
		@button2.Location = System::Drawing::Point.new(146, 152)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(75, 23)
		@button2.TabIndex = 7
		@button2.Text = "clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.BackColor = System::Drawing::Color.Plum
		@button3.Location = System::Drawing::Point.new(249, 152)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(75, 23)
		@button3.TabIndex = 8
		@button3.Text = "off"
		@button3.UseVisualStyleBackColor = false
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.Purple
		self.ClientSize = System::Drawing::Size.new(960, 454)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@label2)
		self.Controls.Add(@label1)
		self.Controls.Add(@button1)
		self.Controls.Add(@textBox4)
		self.Controls.Add(@textBox3)
		self.Controls.Add(@textBox2)
		self.Controls.Add(@textBox1)
		self.Name = "MainForm"
		self.Text = "ave"
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	

	def Button1Click(sender, e)
		num1 = int(textBox1.Text)
		num2 = int(textBox2.Text)
		num3 = int(textBox3.Text)
		num4 = int(textBox4.Text)
		ave = (num1 = num2 + num3 + num4)/ 4
		@label1.Text = "sum: " + str(sum)
		@label2.Text = "ave: " + str(ave)
		
	end

	def Button2Click(sender, e)
		@textBox1.Text = ""
		@textBox2.Text = ""
		@label1.Text = ""
		@label2.Text = ""
	end

	def Button3Click(sender, e)
		Application.Exit()
	end

	
end

