SELECT 
    SUM(scheduled_principal) + SUM(curtailments) + SUM(curtailment_adjustments) + SUM(other_principal_adjustments) + SUM(prepayment) + SUM(repurchase_principal) + SUM(liquidation_principal) + SUM(principal_recoveries) - SUM(principal_losses) AS Total_Principal 
FROM
    last_super_final_test.loandetailcmlt06amc12304;
