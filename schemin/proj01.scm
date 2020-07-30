(define (over-or-under num1 num2)
  (cond
    ((< num1 num2) (- 1))
    ((> num1 num2) 1)
    ((= num1 num2) 0)
  )
)

;;; Tests
(over-or-under 1 2)
; expect -1
(over-or-under 2 1)
; expect 1
(over-or-under 1 1)
; expect 0
(over-or-under 1 1)
; expect 0


(define (g n)
  (if (<= n 3) n (+ (g (- n 1)) (* 2 (g (- n 2))) (* 3 (g (- n 3))))
    )
  )
;;; Tests
(g 1)
; expect 1
(g 2)
; expect 2
(g 4)
; expect 10
(g 5)
; expect 22


(define (composer func)
  (define (func_adder f)
    (composer (lambda n (func (f n)))
	      )
    )
  func func_adder
  )
