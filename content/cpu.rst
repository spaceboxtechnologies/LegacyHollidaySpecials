=================================
The Central Processing Unit (CPU)
=================================
    We are usually taught, probably in elementary school, that the cpu is a box
    that comes bundled with our computer screen (amongst other accessories).
    While it makes some sense to be asked "where is the cpu?" and you point to
    the box (perhaps, you do not have the time or opportunity to open the box),
    this is not technically correct.

    A cpu is a single unit (among many other functional units e.g RAM, ROM etc) embedded in the motherboard, which is itself inside the box. The cpu is considered the brain of a computer as it performs many (depending on the `isa`) simple arithmetic and logical operations which are at the core of what makes a computer what it is. And these days, a cpu does this incredibly fast, in tens of hundreds per second. 

    CPU in action
    =============
        The idea behind a cpu is very simple:
        - pick a problem you want to solve
        with a cpu and it's constituent elements.

        - find a way to represent the elements of that problem(a
        model or code).

        - find a way to implement your found representation (bring it to life).

        - build a system that operates on that model.

        Of the above items, the last one is the hardest and the near exclusive domain of hardcore scientists (call it rocket science). However as software engineer, understanding the first 3 principles and how today's computing and computers fit-in can go a long way in helping you level-up your game in the ever-changing industry. 
        
        Let's demonstrate how today's computers relate to the above items with a
        primitive cpu that only adds numbers, call it legacyCPU and let's tag
        this implementation as version 1.0.

        LegacyCPU v1.0
        --------------

        - Pick a problem and it's elements: We want legacyCPU to be able to add
        numbers. The problem is adding, the element is number.

        - Find a model for the problem element: how can we represent numbers? The
        most popular model (also called number base) for numbers is `decimal` (base 10). We also have other models
        like `binary` (base 2), `octal` (base 8), `hexadecimal` (base 16) etc. Of course we can't just pick any
        model arbitrarily. We want a model that will make our next other steps not just
        possible but easier and more robust. Most modern computers settled for
        `binary`. We will see why.

        - find a way to implement your selected model: Just like many computer
          cpu's, I pick `binary` for my representation of numbers while unlike
          any cpu in existence, I have chosen to implement my cpu using water
          and tubes. Stupid!!!

        - build a system that operates on that model: one beauty of `binary` is
          its stupid simplicity: has only 0 and 1 as its possible values. How
          can we "bring that to life" with tubes and water? Well, I could
          stipulate that "if water is in a tube, that's a 1 otherwise, it's a
          0". Or I could do it vice-versa : "an empty tube is a 1 otherwise, a
          0" but the former makes more sense and easier to reason about.
            
          So, let's make our specification for legacyCPU "simple stupid": it should be
          able to add one binary digit to another one binary digit. With this we
          know the scope of our problem is definite, we should even know all the
          possible permutations of digits we expect to add, all in advance. This is
          usually a rare peek, especially with softwares: your software can be tasked
          to solve problems you never anticipated during its creation. Below is
          a table that explicitly defines the problem's scope:
        
          ======   ======    ===== ======
          digit1 + digit2 =  carry result
          ======   ======    ===== ======
            0       0          0     0
            1       0          0     1
            0       1          0     1
            1       1          1     0


          Or we can notationally depict the above as:
            0      1     1     1
           +0     +0    +0    +1
           ___    ___   ___   ____
            0      1     1     10


          For this my little brain is telling me to use 3 tubes: one tube for
          the first digit, another tube for the other digit and the last for the
          result. 

          ||      ||
          ||      ||
          ||______||
          |___°°___|
              ||
              ||
              ||
              ||

          BOOM! there we go. You can say joined 4 tubes or bent two
          tubes and joined to a third tube, to form a y-shaped structure (I
          don't care). But, notice the horizontal lid covering the single tube
          facing downwards that seeks to prevent water from dripping into it.
          The lid completely the covers the tube. Let's zoom in on that lid to
          understand what it does.

          |                     |
        --°--                |--°--|
        The lead             |     |
                             |     |
                             |     |

                             How the lead
                             covers the down-facing tube



        The lead has a motor that enable the lead turn in one direction at a
        time in response to weight (like a scale). Let's demonstrate this
        mechanism by putting a box on it.

         |               | /
       []|               |/
      |--°--|        |   /  |
      |     |        |[]/   |

      action         result (box slide into the tube).




         |               | /
       []|               |/
      |--°--|        |   /  |
      |     |        |[]/   |

      action         result (box slide into the tube).
