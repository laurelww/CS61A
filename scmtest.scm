;; multiply x by y (without using the * operator).
;; (mulxy 3 4) -> 12 ; 12 = 3 + 3 + 3 + 3
;; (mulxy (- 3) (- 4)) -> 12 ; 12 = - ( -3 + -3 + -3 + -3 )
(define (mulxy x y)
    (cond ((< y 0) (- (mulxy x (- y)) ))
        ((= y 0) 0)
        (else ( + x (mulxy x (- y 1) )))))