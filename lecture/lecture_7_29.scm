(define (reduce procedure s start)
    (if (null? s) start
    (reduce procedure ; this call is a tail
    (cdr s)
    (procedure start (car s)))) ; const space depends on whether procedure requires const space
    ; if procedure req const space, reduce req const spac.
)

;;; Tests
(reduce * '(3 4 5) 2)
; expect 120
(reduce (lambda (x y) (cons y x)) '(3 4 5) '(2))
; expect (5 4 3 2)


; Not tail recursive
(define (map procedure s)
    (if (null? s)
    nil
    (cons (procedure (car s))
          (map procedure (cdr s)))) ; cons is the tail expression, recursion is not
)

;;; Tests
(map (lambda (x) (- 5 x)) (list 1 2))
; expect (4 3)

(define (map procedure s)
    (define (map-reverse s m)
    (if (null? s)
        m
        (map-reverse (cdr s)
                     (cons (procedure (car s))
                     m)))
    )

    (reverse (map-reverse s nil))
)

(define (reverse s)
    (define (reverse-iter s r)
    (if (null? s)
    r
    (reverse-iter (cdr s)
                  (cons (car s) r))))

    (reverse-iter s nil)
)


(define (check expr)
    (list 'if expr ''passed ; if expr == True, return 'passed
        (list 'quote (list 'failed: expr))) ; else quote 'failed and the failed expression
)


;;; For macro
; define a macro that evaluates an expression for each value in a sequence
; scm> (for x '(1 2 3 4) (* x x))
; (1 4 9 16)

(define-macro (for x iter func)
    (define (helper x iter func result)
        (if (null? x)
            result
            (helper (- x 1) (cdr x) func (cons (func (car x)) result))
    )
    (reverse (helper x iter func nil))
)


; prof solution
; define map func
(define (map fn vals)
    (if (null? vals)
    ()
    (cons (fn (car vals)) (map fn (cdr vals)))
    )
)
; scm> (map (lambda (x) (* x x)) '(2 3 4 5))
; (4 9 16 25)

; define macro
(define-macro (for sym vals expr)
    (list 'map (list 'lambda (list sym) expr) vals)
)

; alternate def w cons
(define-macro (for sym vals expr)
    (list 'map 
        (cons 'lambda (cons (cons sym nil) (cons expr nil))) vals)
)

; alternate def w quasiquotation
(define-macro (for sym vals expr)
    `(map (lambda (,sym) ,expr) ,vals))

(for x '(1 2 3) (* x (- x 1)))


; quasiquoting
(define (cadr lst) (car (cdr lst)))
(define (caddr lst) (car (cdr (cdr lst))))
; (1 + 1)         ==> (+ 1 1)
; ((2 * 3) + 4)   ==> (+ (* 2 3) 4)
(define (infix e)
    (if (not (list? e))
        e
        `(,(cadr e) ,(infix (car e)) ,(infix (caddr e))))
)