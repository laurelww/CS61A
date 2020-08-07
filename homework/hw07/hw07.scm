(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)


(define (sign num)
  (cond 
    ((= 0 num) 0)
    ((< 0 num) 1)
    (else (- 1))
        )
)


(define (square x) (* x x))

(define (pow x y)
  (cond
    ((= y 0) 1)  
    ((even? y) (square (pow x (/ y 2))))
    (else (* x (square (pow x (/ (- y 1) 2))))))
)


(define (unique s)
    (cond
        ((null? s) nil)
        (else (cons (car s) 
                    (unique 
                        (filter 
                            (lambda (x) (not (eq? x (car s)))) 
                            (cdr s))))))
)


(define (replicate x n)
  (define (helper x n result)
        (cond
            ((= n 0) result)
            (else (helper x (- n 1) (cons x result)))
        )
      )
  (helper x n nil)
  )


(define (accumulate combiner start n term)
    (cond 
        ((= n 0) start)
        (else (accumulate combiner (combiner (term n) start) (- n 1) term)))
)


(define (accumulate-tail combiner start n term)
    (cond 
        ((= n 0) start)
        (else (accumulate combiner (combiner (term n) start) (- n 1) term)))
)


(define-macro (list-of map-expr for var in lst if filter-expr)
    `(map (lambda (,var) ,map-expr) (filter (lambda (,var) ,filter-expr) ,lst))
)


