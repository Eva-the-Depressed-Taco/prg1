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
		@button1 = System::Windows::Forms::Button.new()
		@textBox1 = System::Windows::Forms::TextBox.new()
		@button2 = System::Windows::Forms::Button.new()
		@button5 = System::Windows::Forms::Button.new()
		@label1 = System::Windows::Forms::Label.new()
		@label2 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.Location = System::Drawing::Point.new(105, 119)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(112, 23)
		@button1.TabIndex = 0
		@button1.Text = "mathify circle"
		@button1.UseVisualStyleBackColor = true
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# textBox1
		# 
		@textBox1.Location = System::Drawing::Point.new(142, 88)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(100, 20)
		@textBox1.TabIndex = 1
		# 
		# button2
		# 
		@button2.Location = System::Drawing::Point.new(142, 149)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(75, 23)
		@button2.TabIndex = 2
		@button2.Text = "clear"
		@button2.UseVisualStyleBackColor = true
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button5
		# 
		@button5.Location = System::Drawing::Point.new(142, 239)
		@button5.Name = "button5"
		@button5.Size = System::Drawing::Size.new(75, 23)
		@button5.TabIndex = 5
		@button5.Text = "off"
		@button5.UseVisualStyleBackColor = true
		@button5.Click { |sender, e| self.Button5Click(sender, e) }
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.Plum
		@label1.Location = System::Drawing::Point.new(272, 119)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(100, 23)
		@label1.TabIndex = 6
		@label1.Text = "label1"
		# 
		# label2
		# 
		@label2.BackColor = System::Drawing::SystemColors.ControlDark
		@label2.Location = System::Drawing::Point.new(272, 149)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(100, 23)
		@label2.TabIndex = 7
		@label2.Text = "label2"
		# 
		# MainForm
		# 
		self.ClientSize = System::Drawing::Size.new(970, 435)
		self.Controls.Add(@label2)
		self.Controls.Add(@label1)
		self.Controls.Add(@button5)
		self.Controls.Add(@button2)
		self.Controls.Add(@textBox1)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "pie"
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	def Button4Click(sender, e)
		@textBox.Text = "I order the food, you cook the food and then the custemer gets the food. we do that for 40 years and then swe die"
	end



	def Button2Click(sender, e)
		@textBox.Text = ""
	end

	def Button5Click(sender, e)
		Application.Exit()
	end

	def Button1Click(sender, e)
	  radius = float(@textBox1.Text)
        area = (radius * radius) * 3.14159
        circum = radius * 2 * 3.14159
        @label1.Text = "Area: " + str(area)
        @label2.Text = "Circum: " + str(circum)   
		
		
	end

	

	def Button2Click(sender, e)
		@label1.Text = ""
        @label2.Text = ""  
		
	end
end

