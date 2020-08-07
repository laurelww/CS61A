(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.

(define (cons-all first rests)
  (map (lambda (x) (cons first x)) rests))

(define (zip pairs)
    (define (helper pairs list1 list2)
        (if (null? pairs) (list list1 list2)
        (helper (cdr pairs) (append list1 (list(caar pairs))) (append list2 (cdar pairs))))
        )
    (helper pairs nil nil)
    )


;; Problem 16
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 16
  (define (helper s idx result)
    (if (null? s) 
        result 
        (helper (cdr s) 
                (+ idx 1) 
                (append result (list (list idx (car s))))))
  )
  (helper s 0 nil)
  )
  ; END PROBLEM 16

;; Problem 17
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  ; BEGIN PROBLEM 17
  (cond ((= 0 total) '(nil))
        ((or (< total 0) (null? denoms)) nil)
        (else (append (cons-all (car denoms) (list-change (- total (car denoms)) denoms)) (list-change total (cdr denoms)))))
)
  ; END PROBLEM 17

;; Problem 18
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 18
         expr
         ; END PROBLEM 18
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 18
         expr
         ; END PROBLEM 18
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 18
           (append `(,form ,params) (map let-to-lambda body))
           ; END PROBLEM 18
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 18
           (append (list `(lambda ,(map let-to-lambda (car (zip values))) ,(car (map let-to-lambda body)))) (map let-to-lambda (cadr (zip values))))
           ; END PROBLEM 18
           ))
        (else
         ; BEGIN PROBLEM 18
         (map let-to-lambda expr)
         ; END PROBLEM 18
         )))



;;; ORIGINAL SKELETON
; ;; Returns a function that checks if an expression is the special form FORM
; (define (check-special form)
;   (lambda (expr) (equal? form (car expr))))

; (define lambda? (check-special 'lambda))
; (define define? (check-special 'define))
; (define quoted? (check-special 'quote))
; (define let?    (check-special 'let))

; ;; Converts all let special forms in EXPR into equivalent forms using lambda
; (define (let-to-lambda expr)
;   (cond ((atom? expr)
;          ; BEGIN PROBLEM 18
;          'replace-this-line
;          ; END PROBLEM 18
;          )
;         ((quoted? expr)
;          ; BEGIN PROBLEM 18
;          'replace-this-line
;          ; END PROBLEM 18
;          )
;         ((or (lambda? expr)
;              (define? expr))
;          (let ((form   (car expr))
;                (params (cadr expr))
;                (body   (cddr expr)))
;            ; BEGIN PROBLEM 18
;            'replace-this-line
;            ; END PROBLEM 18
;            ))
;         ((let? expr)
;          (let ((values (cadr expr))
;                (body   (cddr expr)))
;            ; BEGIN PROBLEM 18
;            'replace-this-line
;            ; END PROBLEM 18
;            ))
;         (else
;          ; BEGIN PROBLEM 18
;          'replace-this-line
;          ; END PROBLEM 18
;          )))