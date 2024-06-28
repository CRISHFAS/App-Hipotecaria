# app.py

from shiny import reactive
from shiny.express import render, input, ui
import faicons as fa
import helpers

# Begin UI --------------------------------------------------------------------
ui.page_opts(fillable=True, title='Interest Calculator App')

with ui.layout_columns(col_widths=(2, 2, 2, 3, 3, 4, 8, 2, 2)):

    # Inputs ----------------------------------------------------------------
    ui.input_numeric("amount", "Amount Financed", 100000, min=1, step=1000) 
    ui.input_numeric("rate", "Interest Rate", 7.25, min=0.01, step=0.05) 
    ui.input_numeric("term", "Term of Loan", 30, min=0.25, step=5) 

    with ui.value_box(showcase=fa.icon_svg("sack-dollar"), theme="bg-gradient-indigo-purple"):
        "Total Paid"

        @render.text
        def total_paid_amount():
            return f'{total_paid():,}'
    
    with ui.value_box(showcase=fa.icon_svg("percent"), theme="bg-gradient-indigo-purple"):
        "Percent Interest"

        @render.text
        def percent_interest():
            return helpers.calculate_percent_interest(input.amount(), total_paid())

    # Editable Table ----------------------------------------------------------------
    amortization_df = reactive.value()

    @reactive.effect
    def _():
        amortization_df.set(
            helpers.make_amortization_table(input.amount(), input.rate(), input.term())
        )

    @render.data_frame
    def payments():
        return render.DataGrid(
            helpers.make_payment_schedule(amortization_df()), 
            editable=True
        )
    
    @payments.set_patch_fn
    def upgrade_patch(*, patch,):
        if patch["column_index"] == 1:
            return helpers.cell_to_float(patch["value"])
        else:
            return patch["value"]

    # Reactive Calcs ----------------------------------------------------------------
    @reactive.calc
    def total_paid():
        return helpers.calculate_total_paid(amortization_df())

    # Plots ----------------------------------------------------------------
    with ui.navset_card_underline():  
        with ui.nav_panel("Cumulative Amount"):
            @render.plot
            def cumulative_plot():
                return helpers.plot_amount_paid_over_time(amortization_df())

        with ui.nav_panel("Payment Composition"):
            @render.plot
            def payments_composition_plot():
                return helpers.plot_payment_composition_over_time(amortization_df())

    ui.input_action_button("update", "Update Payments")
    ui.input_action_button("download", "Download Schedule")

# Update payments schedule -----------------------------------------------------
@reactive.effect
@reactive.event(input.update)
def _():
    updated_schedule = helpers.make_amortization_table(
        input.amount(), 
        input.rate(), 
        input.term(),
        payments.data_view()['Amount'],
        payments.data_view()['Notes']
    )
    amortization_df.set(updated_schedule)
    return None